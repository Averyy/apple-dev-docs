# icon

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The image representing the payment method.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var icon: INImage? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INImage * icon;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INImage * icon;
```

## Discussion

This properties stores an image with any branding information associated with the payment type. For example, this property could contain an image provided by a particular credit card vendor.

## See Also

### Getting the Payment Information
- [var type: INPaymentMethodType](./type.md)
  The type of account used as the source of funds.
- [enum INPaymentMethodType](../inpaymentmethodtype.md)
  Constants describing the available payment options.
- [var name: String?](./name.md)
  The name of this payment type.
- [var identificationHint: String?](./identificationhint.md)
  The hint for identifying the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentmethod/icon)*