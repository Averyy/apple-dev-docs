# ManagedApplicationConfigurationCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The request dictionary to get managed app configurations.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.15+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManagedApplicationConfigurationCommand.Command
```

#### Overview

> **Note**: For a watchOS app, the identifier needs to be the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone to which the watch is paired. Obtain the watch’s bundle identifier for an app with a watch bundle, in the `watchBundleId` key that’s part of the Content Metadata query. For more information on this query, see [`Getting App and Book Information (Legacy)`](getting-app-and-book-information-legacy.md).

For a watchOS app, the identifier needs to be the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone to which the watch is paired. Obtain the watch’s bundle identifier for an app with a watch bundle, in the `watchBundleId` key that’s part of the Content Metadata query. For more information on this query, see [`Getting App and Book Information (Legacy)`](getting-app-and-book-information-legacy.md).

- RequestRequiresNetworkTether: If `true`, the device must be network-tethered to run the command.
- RequestType: The request type to get managed app configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationconfigurationcommand/command-data.dictionary)*