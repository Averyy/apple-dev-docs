# supportsVersion

**Framework**: Apple Pay on the Web  
**Kind**: method

Detects whether a web browser supports a particular Apple Pay version.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
static boolean supportsVersion();
```

## Mentions

- [Apple Pay on the Web Version 4 Release Notes](apple-pay-on-the-web-version-4-release-notes.md)

#### Return Value

A Boolean value that indicates whether the web browser (Safari) supports a particular Apple Pay version. Returns `false` if the web browser does not support the specified version.

#### Discussion

Apple increments the Apple Pay version number when adding new functionality that is not backward compatible with previous versions of Safari. The same Apple Pay version number applies to both Apple Pay JS and Payment Request APIs.

Check version support to ensure new API can run in the user’s browser, and provide fallback to earlier API versions whenever possible for broadest compatibility. See doc://com.apple.documentation/documentation/apple_pay_on_the_web/apple_pay_on_the_web_version_history for the version numbers and detailed information.

## Parameters

- `version`: An integer specifying the Apple Pay version number. For the best compatibility with operating systems and browsers, use the lowest possible version number that supports the features required. See  doc://com.apple.documentation/documentation/apple_pay_on_the_web/apple_pay_on_the_web_version_history  for version numbers and detailed information.

## See Also

- [applePayCapabilities](applepaysession/applepaycapabilities.md)
  Indicates whether the device supports Apple Pay and whether the person has an active card in Wallet that qualifies for web payments.
- [canMakePayments](applepaysession/canmakepayments.md)
  Indicates whether the device supports Apple Pay.
- [canMakePaymentsWithActiveCard](applepaysession/canmakepaymentswithactivecard.md)
  Indicates whether the device supports Apple Pay and whether the user has an active card in Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/supportsversion)*