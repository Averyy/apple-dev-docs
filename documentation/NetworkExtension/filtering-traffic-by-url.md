# Filtering traffic by URL

**Framework**: Network Extension

Perform fast and robust filtering of full URLs by managing URL filtering configurations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- Xcode 26.0+

#### Overview

Filtering requests by URL presents an efficiency challenge because real-world use of URL filters often involves testing against thousands, or even millions, of URLs. To perform this filtering, the Network Extension framework’s URL-filtering API uses two steps:

1. A local *Bloom filter* to rapidly make an initial decision about URLs that aren’t in the filtering set
2. A configured Private Information Retrieval (PIR) server to consult for potential matches

The sample code project `SimpleURLFilter` demonstrates how to use both of these steps to create a working URL filter.

> **Note**: This sample code project is associated with WWDC25 session 234: [`Filter and tunnel network traffic with NetworkExtension`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/234/).

##### Configure the Sample Code Project

To configure the sample code projects, do the following:

1. Open the sample code workspace, `SimpleURLFilter.xcworkspace`, in Xcode. Because the workspace coordinates dependencies between its member projects, always access this sample through its workspace and not the individual projects.
2. In Xcode, select your team as the developer team for all targets so Xcode automatically manages the provisioning profile. For more information, see [`Assign a project to a team`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev23aab79b4).
3. Optionally build and run the PIR server sample described in [`Setting up a PIR server for URL filtering`](setting-up-a-pir-server-for-url-filtering.md). If you have your own PIR server ready for use, you can use that instead.
4. Optionally populate the URL prefilter by using the provided `BloomFilterTool` to create data for both the Bloom filter and the PIR server. The article [`Using the Bloom filter tool to configure a URL filter`](using-the-bloom-filter-tool.md) describes how to use this tool. If you prefer not to do this manually, the sample app extension already has Bloom filter data in the file `bloom_filter.plist` that it can use.

##### Run the Sample

With the PIR server set up, go back to the Xcode workspace to build and run the sample on a macOS or iOS device. The main view of the app shows status information about the currently installed filter, if any, and transient status messages from the app as it performs its actions. The main view also has an Actions menu — available from the menu bar in macOS and a toolbar button in iOS — to provide ancillary functions like cache clearing and configuration reloading.

![A single-window macOS app that represents a running URL filter. A large network badge icon fills most of the space, with text below that reads Running. At the bottom of the window there are two buttons: Disable and Configure. The Configure button is tinted to indicate it’s the default.](/images/com.apple.networkextension/filtering-traffic-by-url-01@2x.png)

This view shows two buttons:

- Enable or Disable offers a quick way to enable or disable the filter configuration.
- Configure presents an interface to view and change the filter properties, and then apply those changes. These properties include enabling or disabling the filter, specifying a URL for the PIR server, and setting the prefilter fetch frequency interval. There’s also a toggle to indicate whether an error causes the filter to allow or deny the URL request that caused the error.

The Privacy Pass server URL is optional in this context. If you don’t specfify a Privacy Pass URL, the system assumes the configured PIR server URL handles this responsibility as well, which is the case for the provided sample server.

For example, if you use the sample PIR server described in [`Setting up a PIR server for URL filtering`](setting-up-a-pir-server-for-url-filtering.md) and run it, you:

- Toggle the Enabled switch to the on state.
- Set the PIR Server URL to `http://localhost:8080`.
- Leave the PIR Privacy Pass Issuer URL field empty.
- Populate the Authentication Token with `AAAA` (as indicated in the sample `service-config.json` file).
- Leave the Pre-filter Fetch Frequency at the default setting of 45 minutes.
- Toggle the Fail Closed switch to the on state.

Use the Apply button to save these configuration changes and start the filter.

> **Note**: When you apply configuration changes, the system prompts you to allow the filter. If you choose to proceed, the system prompts you to enter the device password, and then launches the system Settings app, where you can verify enabling the filter. You can also use the Settings app to enable or disable it later. After approving the filter in the Settings app, return to the `SimpleURLFilter` to monitor its activity or make changes.

After you enable the filter, go to Safari and attempt to load any of the URLs listed in the file `input_urls`, such as `https://example.com`. Loading these URLs should fail immediately with the filter enabled, and potentially succeed with the filter disabled, assuming the host is up and reachable.

##### Provide a View of the Filter Configuration

The sample code workspace contains projects for the `SimpleURLFilter`, the `SwiftBloomFilter` framework it uses to perform prefiltering, and the separate `BloomFilterTool`, which is described in [`Using the Bloom filter tool to configure a URL filter`](using-the-bloom-filter-tool.md). Within the `SimpleURLFilter` project, there are two targets:

- `SimpleURLFilter` is the SwiftUI app that configures and enables the filter.
- `SimpleURLFilterExtension` is the app extension that implements the URL filter by conforming to the [`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md) protocol.

The `SimpleURLFilter` app uses two views. `ContentView` uses a large icon to show the current filter state and offers a button to enable or disable the filter, and another button to configure it. When you tap the Configure button, the `ConfigurationView` slides out as a sheet, offering a form to set filter properties like the PIR server URL and authentication token.

Both of these views depend on a `Configuration` object, which maintains the filter configuration state. The views communicate through a `ConfigurationModel` that contains the `Configuration` as a property. The model uses the [`@Observable`](https://developer.apple.comhttps://developer.apple.com/documentation/observation/observable()) macro to simplify exposing changes in the configuration to the views.

##### Interact with the Filter

The model also contains the property `sharedFilterManager` as a reference to the shared instance of the [`NEURLFilterManager`](neurlfiltermanager.md) class, `NEURLFilterManager.shared`. This is the app’s main interface with the [`URL filters API`](https://developer.apple.comhttps://developer.apple.com/documentation/networkextension/url-filters); setting this object’s properties determines how the URL filter operates.

For example, when someone presses Apply after setting configuration values, the `ConfigurationView` calls the `ConfigurationModel` method `save(configuration:)`. After validating the configuration values, this method calls the filter manager’s [`setConfiguration(pirServerURL:pirPrivacyPassIssuerURL:pirAuthenticationToken:controlProviderBundleIdentifier:)`](neurlfiltermanager/setconfiguration(pirserverurl:pirprivacypassissuerurl:pirauthenticationtoken:controlproviderbundleidentifier:).md) method to pass in the PIR server settings from the `Configuration` object. It also sets other values on the manager, by setting the [`prefilterFetchInterval`](neurlfiltermanager/prefilterfetchinterval.md), [`shouldFailClosed`](neurlfiltermanager/shouldfailclosed.md), and [`isEnabled`](neurlfiltermanager/isenabled.md) properties. Finally, the method calls the manager’s [`saveToPreferences()`](neurlfiltermanager/savetopreferences().md) method, to persist these values for future runs. Here’s the complete `save(configuration:)` method:

```swift
public func save(configuration: Configuration) async throws {
    guard let pirServerURL = configuration.pirServerURL, let pirAuthenticationToken = configuration.pirAuthenticationToken else {
        throw ConfigurationError.badConfiguration
    }

    // Set `controlProviderBundleIdentifier` to a default value, if needed.
    let controlProviderBundleIdentifier = defaultControlProviderBundleIdentifier(given: configuration.controlProviderBundleIdentifier)
    log.debug("Save Configuration: \(configuration.debugDescription) (using controlProviderBundleIdentifier '\(controlProviderBundleIdentifier)')")

    // Set the configuration on the manager, staging it so the system can save it. 
    try sharedFilterManager.setConfiguration(pirServerURL: pirServerURL,
                                             pirPrivacyPassIssuerURL: configuration.pirPrivacyPassIssuerURL,
                                             pirAuthenticationToken: pirAuthenticationToken,
                                             controlProviderBundleIdentifier: controlProviderBundleIdentifier)

    sharedFilterManager.prefilterFetchInterval = configuration.prefilterFetchInterval
    sharedFilterManager.shouldFailClosed = configuration.shouldFailClosed
    sharedFilterManager.isEnabled = configuration.enabled

    do {
        // Save the configuration.
        try await sharedFilterManager.saveToPreferences()
        currentConfiguration = configuration
        log.debug("Saved configuration.")
    } catch NEURLFilterManager.Error.configurationUnchanged {
        // No need to report this as an error to the user, so just log it.
        log.debug("Configuration unchanged.")
    }
}
```

When the app runs again, the model needs to retrieve the saved configuration at launch time, which it does by calling the manager’s [`loadFromPreferences()`](neurlfiltermanager/loadfrompreferences().md) to set the stored values on the shared filter manager. A helper method, `exportConfiguration()`, populates the model’s `Configuration` object with the manager’s various properties, like the PIR-related URLs and behavior properties. This approach allows the view to display and edit those properties, and ultimately save them back to the manager if the person using the app changes them.

```swift
public func loadCurrentConfiguration() async throws {
    // Load the configuration into the manager, and export it as the Configuration object.
    try await sharedFilterManager.loadFromPreferences()
    let configuration = exportConfiguration()
    currentConfiguration = configuration
    log.debug("Loaded current configuration: \(configuration.debugDescription)")
}
```

When the model sets the filter configuration’s various properties, its last step is to set [`isEnabled`](neurlfiltermanager/isenabled.md) to `true` (Swift) or `YES` (Obj-C), and save the configuration to the filter manager. When the system sees that the manager saved preferences with the filter enabled, it attempts to run the filter. This attempt may or may not succeed, depending on the validity of the configuration, whether a valid PIR server exists at the configured address, and other factors. In any case, the [`status`](neurlfiltermanager/status-swift.property.md) updates as the filter changes state, from [`NEURLFilterManager.Status.starting`](neurlfiltermanager/status-swift.enum/starting.md) to [`NEURLFilterManager.Status.running`](neurlfiltermanager/status-swift.enum/running.md) in success cases, or to [`NEURLFilterManager.Status.invalid`](neurlfiltermanager/status-swift.enum/invalid.md) if the configuration is invalid. The filter manager exposes these status changes as an [`AsyncSequence`](https://developer.apple.com/documentation/swift/asyncsequence) of [`NEURLFilterManager.Status`](neurlfiltermanager/status-swift.enum.md) values, through the [`handleStatusChange()`](neurlfiltermanager/handlestatuschange().md) method. The sample’s `ConfigurationModel` calls a `initiateStatusUpdate()` at startup to process these status changes, which it then converts into a custom `FilterStatus` type to facilitate logging and updating the UI.

```swift
private func initiateStatusUpdate() {
    Task {
        for await status in sharedFilterManager.handleStatusChange() {
            let updatedStatus = await FilterStatus(status: status, configuration: currentConfiguration)
            log.debug("Received filter status change: \(String(describing: updatedStatus))")
            filterStatus = updatedStatus
        }
    }
}
```

If the updated status indicates the filter stopped, the sample creates an error message by retrieving the [`lastDisconnectError`](neurlfiltermanager/lastdisconnecterror.md) property from the shared instance of the [`NEURLFilterManager`](neurlfiltermanager.md).

##### Implement the App Extension

Although `SimpleURLFilter` provides a UI to manage the filter, the actual filter is in the `SimpleURLFilterExtension` target. This app extension target defines the `URLFilterControlProvider` class, which implements the [`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md) protocol required for providing a URL filter.

When properly configured, the system calls the provider’s [`fetchPrefilter(existingPrefilterTag:)`](neurlfiltercontrolprovider/fetchprefilter(existingprefiltertag:).md) method, which loads a Bloom filter that functions as a prefilter before consulting the PIR server. This method takes an `existingPrefilterTag` string parameter that the implementation can use to determine whether it already loaded this Bloom filter, or if it needs to do so now. The system calls this method periodically, based on the value of `prefilterFetchInterval` in the configuration, which defaults to 45 minutes. You can use this repeated callback as an opportunity to check for and download an updated Bloom filter from your server, although the sample doesn’t do this.

The implementation in `SimpleURLFilterExtension` uses a custom `BloomFilter` type defined in the sample code project’s `SwiftBloomFilter` framework target. The `BloomFilter` type supports serialization of the Bloom filter data and related metadata as a property list. By default, the project uses a small set of filtered URLs in the file `bloom_filter.plist`. To create a Bloom filter for your own URLs, build the `BloomFilterTool` target and run it from the command line, as described in [`Using the Bloom filter tool to configure a URL filter`](using-the-bloom-filter-tool.md). This approach creates a new property list file for the Bloom filter, as well as a PIR server configuration file with the same URLs.

With the custom `BloomFilter` object initialized, the extension’s implementation of `fetchPrefilter(existingPrefilterTag:)` needs to initialize and return a [`NEURLFilterPrefilter`](neurlfilterprefilter.md) instance. To do this, it needs to provide the filter data — the raw binary of the bitfield used to match URLs against — to the [`NEURLFilterPrefilter`](neurlfilterprefilter.md) initializer. The initializer receives this data as a [`NEURLFilterPrefilter.PrefilterData`](neurlfilterprefilter/prefilterdata.md) type, which allows callers to represent the filter data as either an in-memory [`Data`](https://developer.apple.com/documentation/foundation/data) instance or a [`URL`](https://developer.apple.com/documentation/foundation/url) reference to a file. The sample stores the Bloom filter data in a temporary file, which can avoid memory pressure problems with large datasets.

The following excerpt from the bottom of `fetchPrefilter(existingPrefilterTag:)` shows how the sample saves the `filterData` to a file, then provides this to the [`init(data:tag:bitCount:hashCount:murmurSeed:)`](neurlfilterprefilter/init(data:tag:bitcount:hashcount:murmurseed:).md) initializer by using the [`NEURLFilterPrefilter.PrefilterData.temporaryFilepath(_:)`](neurlfilterprefilter/prefilterdata/temporaryfilepath(_:).md) file wrapper. The sample uses various properties of `filter`, an instance of the custom `BloomFilter` type, to provide the other parameters to the [`NEURLFilterPrefilter`](neurlfilterprefilter.md) initializer.

```swift
let tmpdir = FileManager.default.temporaryDirectory
let fileURL = tmpdir.appendingPathComponent("bloomfilterdata")

do {
    try filterData.write(to: fileURL)
} catch {
    log.error("Unable to write bit vector data to temp file '\(fileURL)'. Error: \(error)")
    return nil
}

let prefilterData: NEURLFilterPrefilter.PrefilterData = .temporaryFilepath(fileURL)
let preFilter = NEURLFilterPrefilter(
    data: prefilterData,
    tag: tag,
    bitCount: Int(filter.bitCount),
    hashCount: Int(filter.hashCount),
    murmurSeed: filter.murmurSeed
)
log.debug("Fetched prefilter with tag '\(tag)'")
return preFilter
```

From the app extension’s point of view, the Bloom filter data itself is opaque; the extension only needs to load it from the property list file. As described in [`Using the Bloom filter tool to configure a URL filter`](using-the-bloom-filter-tool.md), the `BloomFilterTool` target is responsible for actually creating this data, and you can look in the `SwiftBloomFilter` target to inspect the hashing functions that encode the prefilter data.

##### Perform Url Filtering with Mdm

Rather than configuring a URL filter for one device with an app, you can also perform configuation through mobile device management (MDM). This may be a better solution for enterprise deployment and other scenarios where you need to manage a large number of devices with identical configurations.

To perform configuration through MDM, set two properties on the [`WebContentFilter`](https://developer.apple.com/documentation/devicemanagement/webcontentfilter) payload:

| Property | Value |
| --- | --- |
| `FilterURLs` | A Boolean value you set to `true` to enable URL filtering. |
| `URLFilterParameters` | A dictionary containing configuration values for the filter. These include things like the `PIRServerURL` and `URLPrefilterFetchFrequency`. The [`WebContentFilter.URLFilterParameters`](https://developer.apple.com/documentation/devicemanagement/webcontentfilter/urlfilterparameters-data.dictionary) page defines the keys and types that this dictionary accepts. |

## See Also

- [Setting up a PIR server for URL filtering](setting-up-a-pir-server-for-url-filtering.md)
  Configure and run a PIR server to support a URL filter using Apple’s open source container tool.
- [Using the Bloom filter tool to configure a URL filter](using-the-bloom-filter-tool.md)
  Create the files a URL filter needs for its Bloom prefilter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/filtering-traffic-by-url)*