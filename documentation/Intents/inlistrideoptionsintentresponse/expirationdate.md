# expirationDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date after which the specified ride options are no longer valid.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var expirationDate: Date? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSDate * expirationDate;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSDate * expirationDate;
```

#### Discussion

Use this property to specify when the ride options may become invalid. If the user does not select a ride option within the specified expiration date, SiriKit may send a new [`INListRideOptionsIntent`](../inlistrideoptionsintent.md) object to your handler before letting the user choose an option.

If you do not set a value for this property, the ride options do not expire automatically. The system does not necessarily cache ride options until the expiration date. It keeps a reference to them only while the user is viewing them, and may request an updated set of options at any time. Any explicit user request for a list of ride options always results in fresh calls to your handler object to provide that information.

The default value of this property is `nil`.

## See Also

### Accessing the Response Parameters
- [var rideOptions: [INRideOption]?](./rideoptions.md)
  An array of ride options representing the services and prices that you are able to offer.
- [var paymentMethods: [INPaymentMethod]?](./paymentmethods.md)
  An array of payment methods supported by your service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponse/expirationdate)*