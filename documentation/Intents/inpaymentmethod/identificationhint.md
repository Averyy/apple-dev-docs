# identificationHint

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The hint for identifying the payment method.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var identificationHint: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * identificationHint;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * identificationHint;
```

#### Discussion

Use this string in conjunction with the [`name`](./name.md) property to identify the payment method uniquely. For example, this property may contain the last four digits of a credit card number to help distinguish it from other credit cards of the same type.

## See Also

### Getting the Payment Information
- [var type: INPaymentMethodType](./type.md)
  The type of account used as the source of funds.
- [enum INPaymentMethodType](../inpaymentmethodtype.md)
  Constants describing the available payment options.
- [var name: String?](./name.md)
  The name of this payment type.
- [var icon: INImage?](./icon.md)
  The image representing the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentmethod/identificationhint)*