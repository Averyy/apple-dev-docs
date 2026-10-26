# paymentRecord

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The details of the payment transaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var paymentRecord: INPaymentRecord? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INPaymentRecord * paymentRecord;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INPaymentRecord * paymentRecord;
```

#### Discussion

Assign an object to this property that contains the details of the financial transaction. Include as much information as possible in the payment record.

The default value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintentresponse/paymentrecord)*