# shippingMethods

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An array of shipping method objects that describe the supported shipping methods.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var shippingMethods: [PKShippingMethod]? { get set }
```

#### Discussion

The default value is `nil`. See the following example.

Setting the shipping methods:

```objc
NSDecimalNumber *freeAmount = [NSDecimalNumber decimalNumberWithString:@"0.00"];
PKShippingMethod *freeShipping = [PKShippingMethod summaryItemWithLabel:@"Free Shipping" amount:freeAmount];
freeShipping.detail = @"Arrives by July 2";
freeShipping.identifier = @"free";
 
NSDecimalNumber *standardAmount = [NSDecimalNumber decimalNumberWithString:@"3.21"];
PKShippingMethod *standardShipping = [PKShippingMethod summaryItemWithLabel:@"Standard Shipping" amount:standardAmount];
standardShipping.detail = @"Arrives by June 29";
standardShipping.identifier = @"standard";
 
NSDecimalNumber *expressAmount = [NSDecimalNumber decimalNumberWithString:@"24.63"];
PKShippingMethod *expressShipping = [PKShippingMethod summaryItemWithLabel:@"Express Shipping" amount:expressAmount];
expressShipping.detail = @"Ships within 24 hours";
expressShipping.identifier = @"express";
 
paymentRequest.shippingMethods = @[freeShipping, standardShipping, expressShipping];
```

## See Also

- [Displaying a Read-Only Pickup Address](displaying-a-read-only-pickup-address.md)
  Configure a payment request to display a read-only pickup address on the payment sheet.
- [class PKShippingMethod](pkshippingmethod.md)
  An object that defines a shipping method for delivering physical goods.
- [var shippingType: PKShippingType](pkpaymentrequest/shippingtype.md)
  The type of shipping the request uses.
- [var shippingContactEditingMode: PKShippingContactEditingMode](pkpaymentrequest/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.
- [enum PKShippingType](pkshippingtype.md)
  A complete list of valid shipping types.
- [enum PKShippingContactEditingMode](pkshippingcontacteditingmode.md)
  Constants that indicate whether the shipping mode prevents the user from editing fields of the shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/shippingmethods)*