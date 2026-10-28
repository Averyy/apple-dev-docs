# applePay()

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates and returns a payment method object that represents payment through Apple Pay.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func applePay() -> Self
```

```objc
+ (instancetype) applePayPaymentMethod;
```

## Discussion

Use this method to obtain a payment method object for Apple Pay.

## See Also

### Initializing a Payment Object
- [init(type: INPaymentMethodType, name: String?, identificationHint: String?, icon: INImage?)](./init%28type,name,identificationhint,icon%29.md)
  Initializes the payment method object with the specified type and descriptive information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentmethod/applepay())*