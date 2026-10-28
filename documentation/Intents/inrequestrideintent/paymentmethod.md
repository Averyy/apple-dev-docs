# paymentMethod

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user’s requested payment method.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var paymentMethod: INPaymentMethod? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPaymentMethod * paymentMethod;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPaymentMethod * paymentMethod;
```

## Discussion

If the user requests a specific payment method, this property contains that method. When processing payments later, you use the requested payment method to determine how to apply charges for the ride. You are responsible for handling and settling all financial transactions between your service and the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintent/paymentmethod)*