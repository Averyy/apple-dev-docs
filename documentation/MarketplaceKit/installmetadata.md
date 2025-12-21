# InstallMetadata

**Framework**: MarketplaceKit  
**Kind**: struct

Information about a specific app to install or update and the person who initiates it.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct InstallMetadata
```

## Mentions

- [Ingesting an alternative distribution package](ingesting-an-alternative-distribution-package.md)

## Topics

### Initializing an install metadata instance
- [init(account: String, appleItemID: AppleItemID, alternativeDistributionPackage: URL, isUpdate: Bool)](installmetadata/init(account:appleitemid:alternativedistributionpackage:isupdate:).md)
  Initializes an install metadata object with the given app information.
- [init(account: String, appleItemID: AppleItemID, alternativeDistributionPackage: URL, isUpdate: Bool, appShareURL: URL?, requestAgeException: Bool)](installmetadata/init(account:appleitemid:alternativedistributionpackage:isupdate:appshareurl:requestageexception:).md)
  Initializes an install metadata object with the given app information and exception request indicator.
### Inspecting app and account information
- [let appleItemID: AppleItemID](installmetadata/appleitemid.md)
  A unique identifier for the app to install.
- [let alternativeDistributionPackage: URL](installmetadata/alternativedistributionpackage.md)
  A URL to the app’s assembled alternative distribution package.
- [var appShareURL: URL?](installmetadata/appshareurl.md)
  A URL to a product landing page for the app on your marketplace website.
- [let isUpdate: Bool](installmetadata/isupdate.md)
  A Boolean value that indicates whether the installation is an app update.
- [let account: String](installmetadata/account.md)
  A user ID for the person installing the app.
### Requesting an exception
- [var requestAgeException: Bool](installmetadata/requestageexception.md)
  A Boolean value that indicates whether the person needs approval to install the app.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ActionButton](actionbutton.md)
  A user-interface element that enables a person to install, update, or launch apps by tapping the element.
- [struct InstallConfiguration](installconfiguration.md)
  Information that describes a requested app installation or app update.
- [enum InstallConfirmationResult](installconfirmationresult.md)
  Options that indicate whether the installation of an app proceeds when a person interacts with an app installation button.
- [struct BatchInstallConfiguration](batchinstallconfiguration.md)
  Information that describes multiple app installations or app updates.
- [enum BatchInstallConfirmationResult](batchinstallconfirmationresult.md)
  Options that indicate whether the installation of multiple apps proceeds when a person interacts with an app installation button.
- [enum MarketplaceDisplayOption](marketplacedisplayoption.md)
  The kinds of deep links that the operating system makes into your marketplace.
- [protocol MarketplaceSceneDelegate](marketplacescenedelegate.md)
  A delegate that handles deep link requests into your marketplace app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installmetadata)*