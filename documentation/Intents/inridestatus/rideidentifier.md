# rideIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique string that you use to identify the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var rideIdentifier: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * rideIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * rideIdentifier;
```

## Mentions

- [Providing Live Status Updates](../../SiriKit/providing-live-status-updates.md)

## Discussion

Use this property to store an app-specific identifier for the ride. Use this string to identify the ride in your own data structures. This string is not displayed to the user.

After the user books a ride, any status updates related to that ride must include a status object with the same identifier as the originally booked ride. Returning a status object with a different identifier causes Siri and Maps to change their UI, under the assumption that the user completed or canceled the previous ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/rideidentifier)*