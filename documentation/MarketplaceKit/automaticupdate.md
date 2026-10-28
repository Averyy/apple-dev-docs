# AutomaticUpdate

**Framework**: MarketplaceKit  
**Kind**: struct  
**Role**: Structure

Information that describes an app that’s available for update, including a download URL.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct AutomaticUpdate
```

## Overview

Your app’s [`MarketplaceAppExtension`](./marketplaceappextension.md) provides the operating system an instance of this structure when asked via your implementation of the [`automaticUpdates(for:)`](./marketplaceappextension/automaticupdates%28for%29.md) callback.

## Topics

### Initializers
- [init(appleItemID: AppleItemID, alternativeDistributionPackage: URL, account: String, installVerificationToken: String)](./automaticupdate/init%28appleitemid,alternativedistributionpackage,account,installverificationtoken%29.md)
### Instance Properties
- [let account: String](./automaticupdate/account.md)
- [let alternativeDistributionPackage: URL](./automaticupdate/alternativedistributionpackage.md)
- [var appShareURL: URL?](./automaticupdate/appshareurl.md)
- [let appleItemID: AppleItemID](./automaticupdate/appleitemid.md)
- [let installVerificationToken: String](./automaticupdate/installverificationtoken.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### App management
- [class AppLibrary](./applibrary.md)
  A class that represents a catalog of all installed apps, and offers various services for the apps that your marketplace distributes.
- [struct AppVersion](./appversion.md)
  Information that describes an app, including its identifier and version number.
- [struct InstallRequirements](./installrequirements.md)
  An app’s installation criteria for a device.
- [typealias AppleItemID](./appleitemid.md)
  An identifier that represents an app.
- [typealias AppleVersionID](./appleversionid.md)
  An identifier that represents a single app version.
- [let MarketplaceKitURIScheme: String](./marketplacekiturischeme.md)
  A URI scheme that defines an alternative distribution app installation link.
- [struct RequestAppDeletionAction](./requestappdeletionaction.md)
  A SwiftUI environment action that requests the deletion of an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/automaticupdate)*