# init(pickupLocation:dropOffLocation:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified pickup and drop-off locations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(pickupLocation: CLPlacemark?, dropOffLocation: CLPlacemark?)
```

```objc
- (instancetype) initWithPickupLocation:(CLPlacemark *) pickupLocation dropOffLocation:(CLPlacemark *) dropOffLocation;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, Maps creates instances when it requires a list of rides offered by your service. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `pickupLocation`: The starting location of the user.
- `dropOffLocation`: The user’s destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintent/init(pickuplocation:dropofflocation:))*