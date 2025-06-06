# shippingType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The type of shipping the request uses.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var shippingType: PKShippingType { get set }
```

## Mentions

- [Displaying a Read-Only Pickup Address](displaying-a-read-only-pickup-address.md)

#### Discussion

This property sets the labels for the shipping information displayed by the [`PKPaymentAuthorizationViewController`](pkpaymentauthorizationviewcontroller.md) class. The default value is [`PKShippingType.shipping`](pkshippingtype/shipping.md). For a complete list of valid shipping types, see [`PKShippingType`](pkshippingtype.md).

> **Note**:  In iOS 14 and earlier, watchOS 4 and earlier, and Catalyst 14 and earlier, if you’re using a [`PKShippingType.storePickup`](pkshippingtype/storepickup.md) shipping type, you need to manage the shipping information displayed by the payment authorization view controller. By default, the system displays the user’s preferred shipping address. You can set the request’s [`shippingAddress`](pkpaymentrequest/shippingaddress.md) property to the address for your store, or hide the shipping information entirely by setting the [`requiredShippingAddressFields`](pkpaymentrequest/requiredshippingaddressfields.md) property to [`PKAddressFieldNone`](pkaddressfield/pkaddressfieldnone.md).

 In iOS 14 and earlier, watchOS 4 and earlier, and Catalyst 14 and earlier, if you’re using a [`PKShippingType.storePickup`](pkshippingtype/storepickup.md) shipping type, you need to manage the shipping information displayed by the payment authorization view controller. By default, the system displays the user’s preferred shipping address. You can set the request’s [`shippingAddress`](pkpaymentrequest/shippingaddress.md) property to the address for your store, or hide the shipping information entirely by setting the [`requiredShippingAddressFields`](pkpaymentrequest/requiredshippingaddressfields.md) property to [`PKAddressFieldNone`](pkaddressfield/pkaddressfieldnone.md).

## See Also

- [Displaying a Read-Only Pickup Address](displaying-a-read-only-pickup-address.md)
  Configure a payment request to display a read-only pickup address on the payment sheet.
- [var shippingMethods: [PKShippingMethod]?](pkpaymentrequest/shippingmethods.md)
  An array of shipping method objects that describe the supported shipping methods.
- [class PKShippingMethod](pkshippingmethod.md)
  An object that defines a shipping method for delivering physical goods.
- [var shippingContactEditingMode: PKShippingContactEditingMode](pkpaymentrequest/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.
- [enum PKShippingType](pkshippingtype.md)
  A complete list of valid shipping types.
- [enum PKShippingContactEditingMode](pkshippingcontacteditingmode.md)
  Constants that indicate whether the shipping mode prevents the user from editing fields of the shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/shippingtype)*