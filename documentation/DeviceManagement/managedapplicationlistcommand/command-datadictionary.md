# ManagedApplicationListCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get the status of all managed apps on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManagedApplicationListCommand.Command
```

## Properties

- `Identifiers` ([string]): The bundle identifiers of the managed apps to include in the response. > ❗ **Important**:  For a watchOS app, the identifier needs to be the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone to which the watch is paired. Obtain the watch’s bundle identifier for an app with a watch bundle, in the `watchBundleId` key that’s part of the Content Metadata query. For more information on this query, see [`Getting App and Book Information (Legacy)`](getting-app-and-book-information-legacy.md).
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationlistcommand/command-data.dictionary)*