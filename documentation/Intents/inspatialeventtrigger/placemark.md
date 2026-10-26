# placemark

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The location that triggers an event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@NSCopying
var placemark: CLPlacemark { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) CLPlacemark * placemark;
```

*macOS*

```objc
@property (atomic, copy, readonly) CLPlacemark * placemark;
```

#### Discussion

This property is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Trigger Condition
- [var event: INSpatialEvent](./event.md)
  The conditions which trigger an event for the specified location.
- [enum INSpatialEvent](../inspatialevent.md)
  Constants indicating when to deliver location-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspatialeventtrigger/placemark)*