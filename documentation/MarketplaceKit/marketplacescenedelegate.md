# MarketplaceSceneDelegate

**Framework**: MarketplaceKit  
**Kind**: protocol

A delegate that handles deep link requests into your marketplace app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
protocol MarketplaceSceneDelegate
```

#### Overview

The operating system calls your app’s scene delegate to launch your app to a specific screen, such as a search result or specific app page. The display option argument determines the specific screen.

## Topics

### Instance Methods
- [func scene(UIWindowScene, askedToDisplay: MarketplaceDisplayOption)](marketplacescenedelegate/scene(_:askedtodisplay:).md)

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
- [enum MarketplaceDisplayOption](marketplacedisplayoption.md)
  The kinds of deep links that the operating system makes into your marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplacescenedelegate)*