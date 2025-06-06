# InstallConfiguration

**Framework**: MarketplaceKit  
**Kind**: struct

Information that describes a requested app installation or app update.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct InstallConfiguration
```

#### Overview

The [`ActionButton.Action.install(_:)`](actionbutton/action-swift.enum/install(_:).md) enumeration case takes an instance of this structure as a parameter.

## Topics

### Initializers
- [init(install: InstallMetadata, confirmInstall: () async -> InstallConfirmationResult)](installconfiguration/init(install:confirminstall:).md)
### Instance Properties
- [let confirmInstall: () async -> InstallConfirmationResult](installconfiguration/confirminstall.md)
- [let install: InstallMetadata](installconfiguration/install.md)

## See Also

- [class ActionButton](actionbutton.md)
  A user-interface element that enables a person to install, update, or launch apps by tapping the element.
- [struct InstallMetadata](installmetadata.md)
  Information about a specific app to install or update and the person who initiates it.
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

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installconfiguration)*