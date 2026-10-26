# pickupLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The starting location for the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var pickupLocation: CLPlacemark? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) CLPlacemark * pickupLocation;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) CLPlacemark * pickupLocation;
```

#### Discussion

Use this property to specify the location where your driver will pick up the user. Do not include the pickup location in the[`waypoints`](./waypoints.md) property.

The default value of this property is `nil`.

## See Also

### Accessing the Route Information
- [var waypoints: [CLPlacemark]?](./waypoints.md)
  The intermediate waypoints for the journey.
- [var dropOffLocation: CLPlacemark?](./dropofflocation.md)
  The destination of the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/pickuplocation)*