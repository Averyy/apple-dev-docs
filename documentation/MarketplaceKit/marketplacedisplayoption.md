# MarketplaceDisplayOption

**Framework**: MarketplaceKit  
**Kind**: enum

The kinds of deep links that the operating system makes into your marketplace.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum MarketplaceDisplayOption
```

#### Overview

The [`MarketplaceSceneDelegate`](marketplacescenedelegate.md) function [`scene(_:askedToDisplay:)`](marketplacescenedelegate/scene(_:askedtodisplay:).md) accepts a case of this enumeration as a parameter.

## Topics

### Enumeration Cases
- [MarketplaceDisplayOption.authentication(account:)](marketplacedisplayoption/authentication(account:).md)
- [case productPage(appleItemID: AppleItemID, appleVersionID: AppleVersionID?)](marketplacedisplayoption/productpage(appleitemid:appleversionid:).md)
- [MarketplaceDisplayOption.searchResults(query:)](marketplacedisplayoption/searchresults(query:).md)
### Initializers
- [init(from: any Decoder) throws](marketplacedisplayoption/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](marketplacedisplayoption/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [class ActionButton](actionbutton.md)
  A user-interface element that enables a person to install, update, or launch apps by tapping the element.
- [struct InstallMetadata](installmetadata.md)
  Information about a specific app to install or update and the person who initiates it.
- [struct InstallConfiguration](installconfiguration.md)
  Information that describes a requested app installation or app update.
- [enum InstallConfirmationResult](installconfirmationresult.md)
  Options that indicate whether the installation of an app proceeds when a person interacts with an app installation button.
- [struct BatchInstallConfiguration](batchinstallconfiguration.md)
  Information that describes multiple app installations or app updates.
- [enum BatchInstallConfirmationResult](batchinstallconfirmationresult.md)
  Options that indicate whether the installation of multiple apps proceeds when a person interacts with an app installation button.
- [protocol MarketplaceSceneDelegate](marketplacescenedelegate.md)
  A delegate that handles deep link requests into your marketplace app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplacedisplayoption)*