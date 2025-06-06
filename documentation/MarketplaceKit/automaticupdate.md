# AutomaticUpdate

**Framework**: MarketplaceKit  
**Kind**: struct

Information that describes an app that’s available for update, including a download URL.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct AutomaticUpdate
```

#### Overview

Your app’s [`MarketplaceExtension`](marketplaceextension.md) provides the operating system an instance of this structure when asked via your implementation of the [`automaticUpdates(for:)`](marketplaceextension/automaticupdates(for:).md) callback.

## Topics

### Initializers
- [init(appleItemID: AppleItemID, alternativeDistributionPackage: URL, account: String, installVerificationToken: String)](automaticupdate/init(appleitemid:alternativedistributionpackage:account:installverificationtoken:).md)
### Instance Properties
- [let account: String](automaticupdate/account.md)
- [let alternativeDistributionPackage: URL](automaticupdate/alternativedistributionpackage.md)
- [var appShareURL: URL?](automaticupdate/appshareurl.md)
- [let appleItemID: AppleItemID](automaticupdate/appleitemid.md)
- [let installVerificationToken: String](automaticupdate/installverificationtoken.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AppLibrary](applibrary.md)
  An object that manages search characteristics, licensing, and the installation of apps.
- [struct AppVersion](appversion.md)
  Information that describes an app, including its identifier and version number.
- [struct InstallRequirements](installrequirements.md)
  An app’s installation criteria for a device.
- [typealias AppleItemID](appleitemid.md)
  An identifier that represents an app.
- [typealias AppleVersionID](appleversionid.md)
  An identifier that represents a single app version.
- [let MarketplaceKitURIScheme: String](marketplacekiturischeme.md)
  A URI scheme that defines an alternative distribution app installation link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/automaticupdate)*