# init(rideIdentifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified ride identifier.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(rideIdentifier: String)
```

```objc
- (instancetype) initWithRideIdentifier:(NSString *) rideIdentifier;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when the user tries to cancel a ride. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `rideIdentifier`: The unique string that you use to identify the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintent/init(rideidentifier:))*