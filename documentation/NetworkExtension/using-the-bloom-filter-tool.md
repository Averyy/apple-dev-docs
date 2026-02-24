# Using the Bloom filter tool to configure a URL filter

**Framework**: Network Extension

Create the files a URL filter needs for its Bloom prefilter.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- Xcode 26.0+

#### Overview

As described in [`Filtering traffic by URL`](filtering-traffic-by-url.md), the [`URL filters API`](https://developer.apple.comhttps://developer.apple.com/documentation/networkextension/url-filters) depends on a high-performance *Bloom filter* to make an initial assessment of whether to permit a given URL request. The [`NEFilterManager`](nefiltermanager.md) applies the Bloom filter in memory and either permits the URL or relays the request to a [`Private Information Retrieval`](https://developer.apple.comhttps://en.wikipedia.org/wiki/Private_information_retrieval) (PIR) server for futher analysis. This prefiltering approach allows the system to make a rapid decision on the vast majority of URLs. Even if a filter includes a million URLs to deny, the number of possible URLs to allow is greater by many orders of magnitude. For this reason, a prefilter that makes quick decisions for most URLs is a crucial feature for a URL filter.

The `SimpleURLFilter` sample contains a built-in Bloom filter and a configuration for a PIR server that excludes a small list of URLs, like [`https://example.com`](https://developer.apple.comhttps://example.com). To create your own filters, the workspace also includes a command-line tool for creating Bloom filter datasets, `BloomFilterTool`. Use this tool to create prefilter data for arbitrarily large datasets.

> **Note**: This sample code project is associated with WWDC25 session 234: [`Filter and tunnel network traffic with NetworkExtension`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc25/234/).

##### Configure the Sample Code Project

1. In Xcode, set the scheme to build the BloomFilterTool target. This is a macOS-only tool, so you can accept the default destination of My Mac or change it to Any Mac.
2. In Xcode, select your team as the developer team for all targets so Xcode automatically manages the provisioning profile. For more information, see [`Assign a project to a team`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev23aab79b4).

The project contains an optional build phase to generate Swift code representing the Protocol Buffers (Protobuf) serialization used for the PIR database. This build phase uses a command-line utility, `protoc`, from the Apple open source [`Swift Protobuf`](https://developer.apple.comhttps://github.com/apple/swift-protobuf) project. The Xcode developer tools don’t include `protoc` by default, but you can install it by using [`Homebrew`](https://developer.apple.comhttps://brew.sh). With Homebrew installed, perform the following command in Terminal:

```None
brew install swift-protobuf
```

Note that if you choose not to install `protoc`, this build phase fails with a nonfatal error and uses pregenerated code instead.

> 💡 **Tip**: If the build fails with a sandbox `file-read-data` error in the shell script `swift_protobuf.sh`, go to the project’s build settings and search for User Script Sandboxing. This value needs to be `NO` in order for the script to run and the build to succeed.

In Xcode, use Product > Build (Cmd-B) to build the tool. Xcode places the resulting executable in the build products folder. You can access this executable in Xcode by opening the Products folder inside the BloomFilterTool target in the Project navigator. You can navigate to this directory in Terminal, or drag the executable to another location and run it from there.

##### Run the Bloom Filter Tool

Use Xcode’s Product > Run menu item to build and run the tool from within Xcode. This approach uses the `input_urls.txt` from the project file as a list of URLs to add to the filter. The scheme provided with the project also uses the `--verbose` command, so you can view the output in the Xcode console.

You can also run the tool in Terminal with the following command:

```None
./BloomFilterTool input-file
```

The text file `input-file` contains the URLs to add to the filter. Represent each URL to filter on its own line as a string that uses the ASCII character subset for internet host names. Because of this limitation on character encoding, you need to [`Punycode`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc3492.txt) any URLs that don’t conform to the allowed-characters subset.

As described in `NEFilterURLManager`, the URL filter performs sub-URL generation or “fuzzy matching” to filter out related URLs, such as including or excluding a leading `www`, path fragments, or query components. This means you don’t need to include all these variants in your list of input URLs.

If the tool processes the input successfully, it produces two files, which by default it places in the current directory:

- `bloom_filter.plist` is a property list file in the format used by the `SimpleURLFilter` sample code.
- `input.txtpb` is the PIR server configuration file. You can use this for the corresponding PIR server data, as described in [`Setting up a PIR server for URL filtering`](setting-up-a-pir-server-for-url-filtering.md).

You can change the default paths for these output files with command-line flags. Run the tool with the `-h` or `--help` flag to see a complete list of options.

##### Create the Bloom Filter Data

The tool uses the sample’s `SwiftBloomFilter` framework target to write the Bloom filter data as a property list, containing the prefilter data and associated metadata. The sample’s `SimpleURLFilter` app also uses this framework to read in the filter data at runtime and provide it to the [`NEURLFilterManager`](neurlfiltermanager.md). For the `BloomFilterTool`, the target uses the “Create Merged Binary” build setting to include the framework with the command-line executable, as described in [`Configuring your project to use mergeable libraries`](https://developer.apple.com/documentation/Xcode/configuring-your-project-to-use-mergeable-libraries).

The framework’s `BloomFilter` initializer accepts an array of URLs as [`String`](https://developer.apple.com/documentation/Swift/String) instances, along with a `falsePositiveTolerance` value. As shown in the following example, the initializer uses the item count to allocate an appropriately sized bit field as a [`Data`](https://developer.apple.com/documentation/Foundation/Data) instance, relying on the private helper methods `calculateBitCount(itemCount:falsePositiveTolerance)` and `calculateHashCount(itemCount:bitCount)`. It then inserts the items into this bit field one by one.

```swift
internal init(items: [String], falsePositiveTolerance: Double = 0.001, murmurSeed: UInt32) throws {
    let itemCount = items.count
    guard itemCount > 0 else {
        throw BloomFilterError.invalidParameters(message: "items must not be empty")
    }
    guard falsePositiveTolerance > 0.0 && falsePositiveTolerance < 1.0 else {
        throw BloomFilterError.invalidParameters(message: "falsePositiveTolerance must be greater than zero and less than one")
    }

    self.itemCount = itemCount
    self.falsePositiveTolerance = falsePositiveTolerance
    self.murmurSeed = murmurSeed

    bitCount = Self.calculateBitCount(itemCount: itemCount, falsePositiveTolerance: falsePositiveTolerance)
    hashCount = Self.calculateHashCount(itemCount: itemCount, bitCount: bitCount)

    // Create the bit field of an appropriate size.
    byteCount = Self.calculateByteCount(bitCount: bitCount)
    bits = Data(count: byteCount)

    // Create the filter by inserting the given items.
    for item in items {
        try insert(value: item)
    }
}
```

The sample uses the helper method `insert(value:)` to encode each item into the bit field. The implementation of this method uses two hashing functions included with the sample, `fnvHash()` and `murmurHash3(seed:)`. These hashing functions provide the data format required by the [`NEURLFilterManager`](neurlfiltermanager.md) to create an in-memory Bloom filter.

```swift
internal mutating func insert(value: String) throws {
    guard let data = value.data(using: .utf8) else {
        throw BloomFilterError.encodingIssue(message: "Unable to encode string '\(value)' to UTF8")
    }

    for count in 0..<hashCount {
        let fnv = data.fnvHash()
        let murmur = data.murmurHash3(seed: murmurSeed)
        let index = Int((fnv &+ count &* murmur) % bitCount)
        bits.setBit(at: index, to: true)
    }
}
```

## See Also

- [Filtering traffic by URL](filtering-traffic-by-url.md)
  Perform fast and robust filtering of full URLs by managing URL filtering configurations.
- [Setting up a PIR server for URL filtering](setting-up-a-pir-server-for-url-filtering.md)
  Configure and run a PIR server to support a URL filter using Apple’s open source container tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/using-the-bloom-filter-tool)*