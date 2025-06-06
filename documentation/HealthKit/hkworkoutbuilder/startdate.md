# startDate

**Framework**: HealthKit  
**Kind**: property

The workout’s start date and time.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var startDate: Date? { get }
```

## See Also

- [func beginCollection(withStart: Date, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/begincollection(withstart:completion:).md)
  Sets the workout’s start date and begins building the workout.
- [func elapsedTime(at: Date) -> TimeInterval](hkworkoutbuilder/elapsedtime(at:).md)
  Calculates the duration of the workout at the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/startdate)*