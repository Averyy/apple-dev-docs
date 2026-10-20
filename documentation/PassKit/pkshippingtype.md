# PKShippingType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

A complete list of valid shipping types.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum PKShippingType
```

```c
enum PKShippingType : NSUInteger;
```

## Topics

### Constants
- [PKShippingType.shipping](./pkshippingtype/shipping.md)
  Shipping the purchase to the provided address using a third-party shipping company. This is the default shipping type.
- [PKShippingType.delivery](./pkshippingtype/delivery.md)
  Delivering the purchase by the seller (for example, pizza, flower, or furniture delivery).
- [PKShippingType.storePickup](./pkshippingtype/storepickup.md)
  Store pickup of the purchase from the seller’s store.
- [PKShippingType.servicePickup](./pkshippingtype/servicepickup.md)
  Picking up an item from the provided address by the service (for example, transportation or shipping services that provide home pickup).
### Initializers
- [init?(rawValue: UInt)](./pkshippingtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Setting the shipping methods and types
- [Displaying a Read-Only Pickup Address](./displaying-a-read-only-pickup-address.md)
  Configure a payment request to display a read-only pickup address on the payment sheet.
- [var shippingMethods: [PKShippingMethod]?](./pkpaymentrequest/shippingmethods.md)
  An array of shipping method objects that describe the supported shipping methods.
- [class PKShippingMethod](./pkshippingmethod.md)
  An object that defines a shipping method for delivering physical goods.
- [var shippingType: PKShippingType](./pkpaymentrequest/shippingtype.md)
  The type of shipping the request uses.
- [var shippingContactEditingMode: PKShippingContactEditingMode](./pkpaymentrequest/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.
- [enum PKShippingContactEditingMode](./pkshippingcontacteditingmode.md)
  Constants that indicate whether the shipping mode prevents the user from editing fields of the shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshippingtype)*