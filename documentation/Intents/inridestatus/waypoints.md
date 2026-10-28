# waypoints

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The intermediate waypoints for the journey.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var waypoints: [CLPlacemark]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<CLPlacemark *> * waypoints;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<CLPlacemark *> * waypoints;
```

## Discussion

Specifying waypoints is optional. You might include waypoints when a single ride involves multiple stops—for example, to pick up or drop off additional members of the user’s party. Do not include the pickup and drop off locations among the waypoints.

The default value of this property is `nil`.

## See Also

### Accessing the Route Information
- [var pickupLocation: CLPlacemark?](./pickuplocation.md)
  The starting location for the ride.
- [var dropOffLocation: CLPlacemark?](./dropofflocation.md)
  The destination of the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/waypoints)*