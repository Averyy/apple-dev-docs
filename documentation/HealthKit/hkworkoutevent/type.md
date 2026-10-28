# type

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The type of workout event.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var type: HKWorkoutEventType { get }
```

```objc
@property (assign, readonly) HKWorkoutEventType type;
```

## Discussion

For a description of possible events, see [`HKWorkoutEventType`](../hkworkouteventtype.md).

## See Also

### Getting property data
- [var dateInterval: DateInterval](./dateinterval.md)
  The time and duration of the event.
- [var metadata: [String : Any]?](./metadata.md)
  The metadata associated with the workout event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutevent/type)*