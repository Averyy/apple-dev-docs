# ManagedApplicationAttributesCommand.Command

**Framework**: Devicemanagement  
**Kind**: dictionary

The request dictionary to query managed app attributes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManagedApplicationAttributesCommand.Command
```

#### Overview

> **Note**: For a watchOS app, the identifier needs to be the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone to which the watch is paired. Obtain the watch’s bundle identifier for an app with a watch bundle, in the `watchBundleId` key that’s part of the Content Metadata query. For more information on this query, see [`Getting App and Book Information (Legacy)`](getting-app-and-book-information-legacy.md).

- RequestRequiresNetworkTether: If `true`, the device must be network-tethered to run the command.
- RequestType: The request type to query managed app attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationattributescommand/command-data.dictionary)*