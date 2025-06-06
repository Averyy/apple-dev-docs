# ApplePayError

**Framework**: Apple Pay on the Web  
**Kind**: init

Creates an Apple Pay error object.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
new errorCode(
	ApplePayErrorCode errorCode,
	optional ApplePayErrorContactField contactField,
	optional DOMString message
);
```

#### Discussion

[`ApplePayError`](applepayerror.md) objects are created using a constructor, as follows:

```javascript
new ApplePayError("shippingContactInvalid", "postalCode", "ZIP Code is invalid")
```

The contact field, [`ApplePayErrorContactField`](applepayerrorcontactfield.md), and message parameters are optional. Use them to provide more detailed information that can help users resolve problems on the payment sheet. Some error codes do not require a contact field parameter. See [`ApplePayErrorCode`](applepayerrorcode.md) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayerror/applepayerror)*