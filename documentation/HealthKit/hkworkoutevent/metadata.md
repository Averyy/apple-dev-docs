# metadata

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The metadata associated with the workout event.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var metadata: [String : Any]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary<NSString *,id> * metadata;
```

## See Also

### Getting property data
- [var dateInterval: DateInterval](./dateinterval.md)
  The time and duration of the event.
- [var type: HKWorkoutEventType](./type.md)
  The type of workout event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutevent/metadata)*