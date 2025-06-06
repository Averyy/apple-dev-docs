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

### Initializers
- [init(account: String, appleItemID: AppleItemID, alternativeDistributionPackage: URL, isUpdate: Bool)](installmetadata/init(account:appleitemid:alternativedistributionpackage:isupdate:).md)
### Instance Properties
- [let account: String](installmetadata/account.md)
  A user ID for the person installing the app.
- [let alternativeDistributionPackage: URL](installmetadata/alternativedistributionpackage.md)
  A URL to the app’s assembled alternative distribution package.
- [var appShareURL: URL?](installmetadata/appshareurl.md)
  A URL to a product landing page for the app on your marketplace website.
- [let appleItemID: AppleItemID](installmetadata/appleitemid.md)
- [let isUpdate: Bool](installmetadata/isupdate.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

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