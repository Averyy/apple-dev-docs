# Apple Pay on the Web Version 4 Release Notes

**Framework**: Apple Pay on the Web

The version of Apple Pay available in macOS 10.14.1 and iOS 12.1.

#### Overview

New features include:

- Added support for a zero [`total`](applepaypaymentrequest/total.md) in [`ApplePayPaymentRequest`](applepaypaymentrequest.md). In versions of Apple Pay JS prior to version 4, the amount of the total must be greater than zero. Check for version availability using [`supportsVersion`](applepaysession/supportsversion.md) before setting a zero amount.
- Added support for new Apple Pay buttons including `book`, `subscribe`, and `check-out`. See [`Displaying Apple Pay Buttons Using CSS`](https://developer.apple.com/documentation/apple_pay_on_the_web/displaying_apple_pay_buttons_using_css) for more information.
- Added the following supported networks: `cartesBancaires`, `eftpos`, `electron`, `maestro`, and `vPay`. See [`supportedNetworks`](applepayrequest/supportednetworks.md) for more information.

## See Also

- [Apple Pay on the Web Version 14 Release Notes](apple-pay-on-the-web-version-14-release-notes.md)
  The version of Apple Pay available in macOS 13 and iOS 16.
- [Apple Pay on the Web Version 13 Release Notes](apple-pay-on-the-web-version-13-release-notes.md)
  The version of Apple Pay available in macOS 12.3 and iOS 15.4.
- [Apple Pay on the Web Version 12 Release Notes](apple-pay-on-the-web-version-12-release-notes.md)
  The version of Apple Pay available in macOS 12 and iOS 15.
- [Apple Pay on the Web Version 11 Release Notes](apple-pay-on-the-web-version-11-release-notes.md)
  The version of Apple Pay available in macOS 11.5 and iOS 14.5.
- [Apple Pay on the Web Version 10 Release Notes](apple-pay-on-the-web-version-10-release-notes.md)
  The version of Apple Pay available in macOS 11 and iOS 14.
- [Apple Pay on the Web Version 9 Release Notes](apple-pay-on-the-web-version-9-release-notes.md)
  The version of Apple Pay available in macOS 10.15.6 and iOS 13.6.
- [Apple Pay on the Web Version 8 Release Notes](apple-pay-on-the-web-version-8-release-notes.md)
  The version of Apple Pay available in macOS 10.15.1 and iOS 13.2.
- [Apple Pay on the Web Version 7 Release Notes](apple-pay-on-the-web-version-7-release-notes.md)
  The version of Apple Pay available in macOS 10.14.6 and iOS 12.4.
- [Apple Pay on the Web Version 6 Release Notes](apple-pay-on-the-web-version-6-release-notes.md)
  The version of Apple Pay available in macOS 10.14.4 and iOS 12.2.
- [Apple Pay on the Web Version 5 Release Notes](apple-pay-on-the-web-version-5-release-notes.md)
  The version of Apple Pay available in macOS 10.14.2 and iOS 12.1.1.
- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)
  The version of Apple Pay available in macOS 10.13 and iOS 11.
- [Apple Pay on the Web Version 2 Release Notes](apple-pay-on-the-web-version-2-release-notes.md)
  The version of Apple Pay available in macOS 10.12.1 and iOS 10.1.
- [Apple Pay on the Web Version 1 Release Notes](apple-pay-on-the-web-version-1-release-notes.md)
  The version of Apple Pay available in macOS 10.12 and iOS 10.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/apple-pay-on-the-web-version-4-release-notes)*