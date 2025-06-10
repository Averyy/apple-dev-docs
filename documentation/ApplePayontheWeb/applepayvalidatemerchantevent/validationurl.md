# validationURL

**Framework**: Apple Pay on the Web  
**Kind**: property

The URL your server must use to validate itself and obtain a merchant session object.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
readonly attribute DOMString validationURL;
```

## Mentions

- [Providing Merchant Validation](providing-merchant-validation.md)

#### Discussion

This attribute is contained by the [`onvalidatemerchant`](applepaysession/onvalidatemerchant.md) event. Access this attribute using the event parameter, for example, `var URL = event.validationURL;`.

Pass the URL in the [`validationURL`](applepayvalidatemerchantevent/validationurl.md) attribute to your server, as described in [`Providing Merchant Validation`](providing-merchant-validation.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayvalidatemerchantevent/validationurl)*