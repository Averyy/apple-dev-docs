# rideIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier that you assigned to the ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var rideIdentifier: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * rideIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * rideIdentifier;
```

#### Discussion

SiriKit sets this property to the ride identifier you provided in your [`INRideStatus`](../inridestatus.md) object when booking the ride or supplying its status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintent/rideidentifier)*