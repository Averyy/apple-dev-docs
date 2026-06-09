# ManagedApplicationAttributesCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to query attributes in managed apps on a device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ManagedApplicationAttributesCommand.Command
```

## Properties

- `Identifiers` ([string]) *(required)*: The bundle identifiers of the managed apps. > ❗ **Important**:  For a watchOS app, the identifier needs to be the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone to which the watch is paired. Obtain the watch’s bundle identifier for an app with a watch bundle, in the `watchBundleId` key that’s part of the Content Metadata query. For more information on this query, see [`Getting app and book information (Legacy)`](getting-app-and-book-information-legacy.md).
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationattributescommand/command-data.dictionary)*