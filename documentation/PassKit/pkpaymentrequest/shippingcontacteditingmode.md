# shippingContactEditingMode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A value that indicates whether the shipping mode prevents the user from editing the shipping address.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var shippingContactEditingMode: PKShippingContactEditingMode { get set }
```

```objc
@property (nonatomic, assign) PKShippingContactEditingMode shippingContactEditingMode;
```

## Mentions

- [Displaying a Read-Only Pickup Address](../displaying-a-read-only-pickup-address.md)

## Discussion

Set the value to [`PKShippingContactEditingMode.storePickup`](../pkshippingcontacteditingmode/storepickup.md) for an in-store or other pickup to prevent the user from editing the shipping address.

For more information on configuring a package for store pickup, see [Displaying a Read-Only Pickup Address](../displaying-a-read-only-pickup-address.md).

> **Note**:  Determine whether to disable editing of the shipping contact field before displaying the payment sheet. Switching from a noneditable to an editable shipping contact field requires the user to restart the payment process.

## See Also

### Setting the shipping methods and types
- [Displaying a Read-Only Pickup Address](../displaying-a-read-only-pickup-address.md)
  Configure a payment request to display a read-only pickup address on the payment sheet.
- [var shippingMethods: [PKShippingMethod]?](./shippingmethods.md)
  An array of shipping method objects that describe the supported shipping methods.
- [class PKShippingMethod](../pkshippingmethod.md)
  An object that defines a shipping method for delivering physical goods.
- [var shippingType: PKShippingType](./shippingtype.md)
  The type of shipping the request uses.
- [enum PKShippingType](../pkshippingtype.md)
  A complete list of valid shipping types.
- [enum PKShippingContactEditingMode](../pkshippingcontacteditingmode.md)
  Constants that indicate whether the shipping mode prevents the user from editing fields of the shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/shippingcontacteditingmode)*