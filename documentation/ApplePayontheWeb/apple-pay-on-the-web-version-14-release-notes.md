# Apple Pay on the Web Version 14 Release Notes

**Framework**: Apple Pay on the Web

The version of Apple Pay available in macOS 13 and iOS 16.

#### Overview

New features include:

- Added support for automatic reload payments, recurring payment requests, and multiple payment tokens in [`ApplePayModifier`](applepaymodifier.md) and [`ApplePayPaymentRequest`](applepaypaymentrequest.md). See [`automaticReloadPaymentRequest`](applepaymodifier/automaticreloadpaymentrequest.md), [`recurringPaymentRequest`](applepaymodifier/recurringpaymentrequest.md) and [`multiTokenContexts`](applepaymodifier/multitokencontexts.md) for more information for `Payment Request API`. See [`automaticReloadPaymentRequest`](applepaypaymentrequest/automaticreloadpaymentrequest.md), [`recurringPaymentRequest`](applepaypaymentrequest/recurringpaymentrequest.md), and [`multiTokenContexts`](applepaypaymentrequest/multitokencontexts.md) for more information for [`Apple Pay JS API`](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api).
- Added support to [`ApplePayPaymentTiming`](applepaypaymenttiming.md) by including an automaticReload value that specifies that the payment occurs automatically.
- Added support for merchants to provide order details of a purchase that’s viewable in Wallet using [`ApplePayPaymentCompleteDetails`](applepaypaymentcompletedetails.md).
- Added `bancomat` and `bancontact` to supported networks. For more information, see [`supportedNetworks`](applepayrequest/supportednetworks.md).

## See Also

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
- [Apple Pay on the Web Version 4 Release Notes](apple-pay-on-the-web-version-4-release-notes.md)
  The version of Apple Pay available in macOS 10.14.1 and iOS 12.1.
- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)
  The version of Apple Pay available in macOS 10.13 and iOS 11.
- [Apple Pay on the Web Version 2 Release Notes](apple-pay-on-the-web-version-2-release-notes.md)
  The version of Apple Pay available in macOS 10.12.1 and iOS 10.1.
- [Apple Pay on the Web Version 1 Release Notes](apple-pay-on-the-web-version-1-release-notes.md)
  The version of Apple Pay available in macOS 10.12 and iOS 10.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/apple-pay-on-the-web-version-14-release-notes)*