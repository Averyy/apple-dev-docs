# dropOffLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The destination of the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var dropOffLocation: CLPlacemark? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) CLPlacemark * dropOffLocation;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) CLPlacemark * dropOffLocation;
```

## Discussion

Use this property to specify the final destination for the ride. Do not include the pickup location in the[`waypoints`](./waypoints.md) property.

The default value of this property is `nil`.

## See Also

### Accessing the Route Information
- [var pickupLocation: CLPlacemark?](./pickuplocation.md)
  The starting location for the ride.
- [var waypoints: [CLPlacemark]?](./waypoints.md)
  The intermediate waypoints for the journey.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/dropofflocation)*