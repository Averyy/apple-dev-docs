# Setting up a PIR server for URL filtering

**Framework**: Network Extension

Configure and run a PIR server to support a URL filter using Apple’s open source container tool.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- Xcode 26.0+

#### Overview

As described in [`Filtering traffic by URL`](filtering-traffic-by-url.md), a Network Extension URL filter uses a Private Information Retrieval (PIR) server as part of a complete URL filtering system. The on-device URL filter evaluates a URL request against a local Bloom prefilter for matches against a list of URLs, providing quick results when evaluating URLs that aren’t in the filter list. For URL requests that the Bloom filter can’t trivially exclude, the URL filter then consults a PIR server to make a final decision.

The sample code project `SimpleURLFilter` contains a PIR server for use with the `SimpleURLFilter` app and its `SimpleURLFilterExtension` app extension. Using a PIR server gives the app a means to query the server while maintaining user privacy.

> **Note**: This sample code project is associated with WWDC25 session 234: [`Filter and tunnel network traffic with NetworkExtension`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc25/234/).

##### Configure the Sample Code Project

The sample code zip file includes the server’s data and configuration files in the directory `PIR Server`. This directory is a sibling to the sample’s Xcode targets (`SimpleURLFilter`, `SwiftBloomFilter`, and `BloomFilterTool`) but isn’t part of the Xcode workspace because you don’t build it with Xcode. Instead, you can use the included `Dockerfile` with various platform-as-a-service systems. If you don’t already have one of these package-deployment systems, you can use Apple’s open source [`container`](https://developer.apple.comhttps://github.com/apple/container) project.

To use `container`, start by downloading and installing `container` from the project’s [`release page`](https://developer.apple.comhttps://github.com/apple/container/releases). Keep in mind that `container` requires macOS 26 or later.

In Terminal, start `container` with the following command:

```None
container system start
```

The PIR server requires that its `usecase` name matches the bundle identifier of the app that connects to the server. By default, the server configuration uses `com.example.apple-samplecode.SimpleURLFilter.url.filtering`. However, this value doesn’t match your app’s bundle identifier because the sample code project adds your team ID to the bundle identifier to disambiguate it from other developers building and running the sample.

So, if you haven’t already, open the `SimpleURLFilter.xcworkspace` in Xcode, and set the development team for the `SimpleURLFilterExtension` target. This action changes the bundle identifier in the Signing & Capabilities tab to something like `com.example.apple-samplecode.SimpleURLFilter1234567890.SimpleURLFilterExtension`. Copy this value to the clipboard, then open `PIR Server/service-config.json` in Xcode or another text editor. Find the `usecases/name` key-value pair in this JSON file, and paste in the correct identifier, making sure to append `.url.filtering` to the value.

Now that the configuration file is correct, you can build the server. Navigate to the PIR Server directory and build the PIR server as follows:

```None
container build -t pir-server .
```

Running the server in place uses the contents of the provided `data` directory, which contains two items:

To customize the database with your own list of filtered URLs, run the `BloomFilterTool` as described in [`Using the Bloom filter tool to configure a URL filter`](using-the-bloom-filter-tool.md). You can take the `input.txtpb` database file created by that tool and use it to replace the default version in the `data` directory.

##### Run the Server

After you successfully build the server, you can run it in `container` with the following command:

```None
container run --remove -d -p 8080:8080 --name pir-server pir-server
```

This command runs the container image tagged `pir-server`, and names the instance `pir-server`, telling the container process to remove the instance after it stops executing. It also maps port `8080` of the host to port `8080` of the container, making the server available at port `8080` on the host.

If you now build and run the `SimpleURLFilter` sample app in Xcode on macOS, you can configure its PIR server URL as `http://localhost:8080`, as described in [`Filtering traffic by URL`](filtering-traffic-by-url.md). If you run the app on iOS instead, use your Mac’s IP address in the URL. For example, if your Mac has the address 192.168.1.2, enter `http://192.168.1.2:8080` when configuring the PIR server URL in the `SimpleURLFilter` app on your iOS device.

##### View Server Log Messages

The command to run the server used the `-d` option to detach from the process, allowing control to return to the terminal immediately. However, this means that logging output doesn’t go to the terminal. Instead, follow `pir-server`’s output with the following command:

```None
container logs --follow pir-server
```

Following the log messages continues until the server stops, or you signal the `follow` command to stop by pressing Control-c.

##### Stop the Server

To stop the server itself, use the following command:

```None
container stop pir-server
```

If you used the `--remove` option to run the server, this also removes the stopped container automatically.

## See Also

- [Filtering traffic by URL](filtering-traffic-by-url.md)
  Perform fast and robust filtering of full URLs by managing URL filtering configurations.
- [Using the Bloom filter tool to configure a URL filter](using-the-bloom-filter-tool.md)
  Create the files a URL filter needs for its Bloom prefilter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/setting-up-a-pir-server-for-url-filtering)*