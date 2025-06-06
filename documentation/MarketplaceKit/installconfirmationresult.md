# InstallConfirmationResult

**Framework**: MarketplaceKit  
**Kind**: enum

Options that indicate whether the installation of an app proceeds when a person interacts with an app installation button.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum InstallConfirmationResult
```

#### Overview

The [`InstallConfiguration`](installconfiguration.md) initializer [`init(install:confirmInstall:)`](installconfiguration/init(install:confirminstall:).md) takes a closure as a parameter that returns a case of this enumeration.

Your marketplace app supplies code in the closure that facilitates any prerequisites a person needs to satisfy to download the app, such as completing a payment flow. The result of the prerequisites flow helps you determine the case to return, ([`InstallConfirmationResult.cancel`](installconfirmationresult/cancel.md) or [`InstallConfirmationResult.confirmed(installVerificationToken:authenticationContext:)`](installconfirmationresult/confirmed(installverificationtoken:authenticationcontext:).md).

## Topics

### Enumeration Cases
- [InstallConfirmationResult.cancel](installconfirmationresult/cancel.md)
- [InstallConfirmationResult.confirmed(installVerificationToken:authenticationContext:)](installconfirmationresult/confirmed(installverificationtoken:authenticationcontext:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [class ActionButton](actionbutton.md)
  A user-interface element that enables a person to install, update, or launch apps by tapping the element.
- [struct InstallMetadata](installmetadata.md)
  Information about a specific app to install or update and the person who initiates it.
- [struct InstallConfiguration](installconfiguration.md)
  Information that describes a requested app installation or app update.
- [struct BatchInstallConfiguration](batchinstallconfiguration.md)
  Information that describes multiple app installations or app updates.
- [enum BatchInstallConfirmationResult](batchinstallconfirmationresult.md)
  Options that indicate whether the installation of multiple apps proceeds when a person interacts with an app installation button.
- [enum MarketplaceDisplayOption](marketplacedisplayoption.md)
  The kinds of deep links that the operating system makes into your marketplace.
- [protocol MarketplaceSceneDelegate](marketplacescenedelegate.md)
  A delegate that handles deep link requests into your marketplace app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installconfirmationresult)*