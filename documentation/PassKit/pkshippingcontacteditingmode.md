# PKShippingContactEditingMode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

Constants that indicate whether the shipping mode prevents the user from editing fields of the shipping address.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum PKShippingContactEditingMode
```

## Topics

### Reading the editing mode
- [PKShippingContactEditingMode.available](pkshippingcontacteditingmode/available.md)
  The value that indicates Apple Pay Later is available.
- [PKShippingContactEditingMode.storePickup](pkshippingcontacteditingmode/storepickup.md)
  The shipping contact on the payment sheet represents a pickup address and isn’t editable by the user.
### Initializers
- [init?(rawValue: UInt)](pkshippingcontacteditingmode/init(rawvalue:).md)
### Type Properties
- [static var enabled: PKShippingContactEditingMode](pkshippingcontacteditingmode/enabled.md)
  All fields of the shipping contact on the payment sheet are editable by the user.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Displaying a Read-Only Pickup Address](displaying-a-read-only-pickup-address.md)
  Configure a payment request to display a read-only pickup address on the payment sheet.
- [var shippingMethods: [PKShippingMethod]?](pkpaymentrequest/shippingmethods.md)
  An array of shipping method objects that describe the supported shipping methods.
- [class PKShippingMethod](pkshippingmethod.md)
  An object that defines a shipping method for delivering physical goods.
- [var shippingType: PKShippingType](pkpaymentrequest/shippingtype.md)
  The type of shipping the request uses.
- [var shippingContactEditingMode: PKShippingContactEditingMode](pkpaymentrequest/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.
- [enum PKShippingType](pkshippingtype.md)
  A complete list of valid shipping types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshippingcontacteditingmode)*