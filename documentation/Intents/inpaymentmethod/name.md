# name

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of this payment type.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var name: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * name;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * name;
```

#### Discussion

Use this property in conjunction with the [`identificationHint`](./identificationhint.md) property to identify each payment method uniquely.

## See Also

### Getting the Payment Information
- [var type: INPaymentMethodType](./type.md)
  The type of account used as the source of funds.
- [enum INPaymentMethodType](../inpaymentmethodtype.md)
  Constants describing the available payment options.
- [var identificationHint: String?](./identificationhint.md)
  The hint for identifying the payment method.
- [var icon: INImage?](./icon.md)
  The image representing the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentmethod/name)*