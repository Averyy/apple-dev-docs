# paymentMethods

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of payment methods supported by your service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var paymentMethods: [INPaymentMethod]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INPaymentMethod *> * paymentMethods;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INPaymentMethod *> * paymentMethods;
```

#### Discussion

Use this property to inform the user about the forms of payment that you accept. The default value of this property is `nil`, which results in no displayed payment method information.

## See Also

### Accessing the Response Parameters
- [var rideOptions: [INRideOption]?](./rideoptions.md)
  An array of ride options representing the services and prices that you are able to offer.
- [var expirationDate: Date?](./expirationdate.md)
  The date after which the specified ride options are no longer valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponse/paymentmethods)*