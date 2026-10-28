# event

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The conditions which trigger an event for the specified location.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var event: INSpatialEvent { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INSpatialEvent event;
```

*macOS*

```objc
@property (atomic, assign, readonly) INSpatialEvent event;
```

## Discussion

The user can trigger events when they leave or arrive at the specified location. This property is set at automatically at initialization time and cacan’tnnot be changed later.

## See Also

### Getting the Trigger Condition
- [var placemark: CLPlacemark](./placemark.md)
  The location that triggers an event.
- [enum INSpatialEvent](../inspatialevent.md)
  Constants indicating when to deliver location-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspatialeventtrigger/event)*