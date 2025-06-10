# ApplePaySession

**Framework**: Apple Pay on the Web  
**Kind**: init

The entry point for Apple Pay on the web.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
new ApplePaySession();
```

## Mentions

- [Apple Pay on the Web Version 12 Release Notes](apple-pay-on-the-web-version-12-release-notes.md)
- [Creating an Apple Pay Session](creating-an-apple-pay-session.md)

#### Discussion

Creating an `ApplePaySession` object throws a JavaScript exception if any of the following occur:

- Any Apple Pay JS API is called from an insecure page.
- You pass an invalid payment request. Payment requests are invalid if they contain missing, unknown, or invalid properties, or if the total is zero or less.
- You attempt to create [`ApplePaySession`](applepaysession.md) outside of a gesture handler.

Check [`supportsVersion`](applepaysession/supportsversion.md) before using any Apple Pay JS API that depends on Safari to support a particular version number.

## Parameters

- `version`: The Apple Pay version number your website supports. See  doc://com.apple.documentation/documentation/apple_pay_on_the_web/apple_pay_on_the_web_version_history  for version information.
- `paymentRequest`: An   object that contains the information to be displayed on the Apple Pay payment sheet.

## See Also

- [begin](applepaysession/begin.md)
  Begins the merchant validation process.
- [supportsVersion](applepaysession/supportsversion.md)
  Detects whether a web browser supports a particular Apple Pay version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/applepaysession)*