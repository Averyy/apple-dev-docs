# type

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of account used as the source of funds.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var type: INPaymentMethodType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INPaymentMethodType type;
```

*macOS*

```objc
@property (atomic, assign, readonly) INPaymentMethodType type;
```

## See Also

### Getting the Payment Information
- [enum INPaymentMethodType](../inpaymentmethodtype.md)
  Constants describing the available payment options.
- [var name: String?](./name.md)
  The name of this payment type.
- [var identificationHint: String?](./identificationhint.md)
  The hint for identifying the payment method.
- [var icon: INImage?](./icon.md)
  The image representing the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentmethod/type)*