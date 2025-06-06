# Apple Pay on the Web Version 3 Release Notes

**Framework**: Apple Pay on the Web

The version of Apple Pay available in macOS 10.13 and iOS 11.

#### Overview

New features include:

- New error handling provided using [`ApplePayError`](applepayerror.md).
- To support enhanced error handling, the number and type of arguments were changed for the following completion methods:

| Method | Argument for Version 3 | Arguments for Versions 1 and 2 |
| --- | --- | --- |
| [`completePaymentMethodSelection`](applepaysession/completepaymentmethodselection.md) | [`ApplePayPaymentMethodUpdate`](applepaypaymentmethodupdate.md) | [`completePaymentMethodSelection in Apple Pay JS API versions 1 and 2`](applepaysession/completepaymentmethodselection#completePaymentMethodSelection-in-Apple-Pay-JS-API-versions-1-and-2.md) |
| [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) | [`ApplePayShippingContactUpdate`](applepayshippingcontactupdate.md) | [`completeShippingContactSelection in Apple Pay JS version 1 and 2`](applepaysession/completeshippingcontactselection#completeShippingContactSelection-in-Apple-Pay-JS-version-1-and-2.md) |
| [`completeShippingMethodSelection`](applepaysession/completeshippingmethodselection.md) | [`ApplePayShippingMethodUpdate`](applepayshippingmethodupdate.md) | [`completeShippingMethodSelection in Apple Pay JS API version 1 and 2`](applepaysession/completeshippingmethodselection#completeShippingMethodSelection-in-Apple-Pay-JS-API-version-1-and-2.md) |
| [`completePayment`](applepaysession/completepayment.md) | [`ApplePayPaymentAuthorizationResult`](applepaypaymentauthorizationresult.md) | [`completePayment in Apple Pay JS API version 1 and 2`](applepaysession/completepayment#completePayment-in-Apple-Pay-JS-API-version-1-and-2.md) |

- Support added for phonetic names in contact information, including `phoneticName` in [`ApplePayContactField`](applepaycontactfield.md); [`phoneticFamilyName`](applepaypaymentcontact/phoneticfamilyname.md) and [`phoneticGivenName`](applepaypaymentcontact/phoneticgivenname.md) in [`ApplePayPaymentContact`](applepaypaymentcontact.md).
- Added a new property to [`ApplePayPaymentRequest`](applepaypaymentrequest.md) called [`supportedCountries`](applepaypaymentrequest/supportedcountries.md) that lets you limit payments to cards from specific countries.

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
- [Apple Pay on the Web Version 4 Release Notes](apple-pay-on-the-web-version-4-release-notes.md)
  The version of Apple Pay available in macOS 10.14.1 and iOS 12.1.
- [Apple Pay on the Web Version 2 Release Notes](apple-pay-on-the-web-version-2-release-notes.md)
  The version of Apple Pay available in macOS 10.12.1 and iOS 10.1.
- [Apple Pay on the Web Version 1 Release Notes](apple-pay-on-the-web-version-1-release-notes.md)
  The version of Apple Pay available in macOS 10.12 and iOS 10.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/apple-pay-on-the-web-version-3-release-notes)*