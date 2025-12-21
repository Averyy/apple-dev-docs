# AppVersion

**Framework**: MarketplaceKit  
**Kind**: struct

Information that describes an app, including its identifier and version number.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct AppVersion
```

#### Overview

Your app’s [`MarketplaceAppExtension`](marketplaceappextension.md) provides the operating system an instance of this structure when asked via your implementation of the [`availableAppVersions(forAppleItemIDs:)`](marketplaceappextension/availableappversions(forappleitemids:).md) callback.

## Topics

### Initializers
- [init(appleItemID: AppleItemID, appleVersionID: UInt64)](appversion/init(appleitemid:appleversionid:).md)
### Instance Properties
- [let appleItemID: AppleItemID](appversion/appleitemid.md)
- [let appleVersionID: UInt64](appversion/appleversionid.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AppLibrary](applibrary.md)
  A class that represents a catalog of all installed apps, and offers various services for the apps that your marketplace distributes.
- [struct AutomaticUpdate](automaticupdate.md)
  Information that describes an app that’s available for update, including a download URL.
- [struct InstallRequirements](installrequirements.md)
  An app’s installation criteria for a device.
- [typealias AppleItemID](appleitemid.md)
  An identifier that represents an app.
- [typealias AppleVersionID](appleversionid.md)
  An identifier that represents a single app version.
- [let MarketplaceKitURIScheme: String](marketplacekiturischeme.md)
  A URI scheme that defines an alternative distribution app installation link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/appversion)*