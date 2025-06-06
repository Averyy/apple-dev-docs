# beginCollection(withStart:completion:)

**Framework**: HealthKit  
**Kind**: method

Sets the workout’s start date and begins building the workout.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func beginCollection(at startDate: Date) async throws
```

## See Also

- [var startDate: Date?](hkworkoutbuilder/startdate.md)
  The workout’s start date and time.
- [func elapsedTime(at: Date) -> TimeInterval](hkworkoutbuilder/elapsedtime(at:).md)
  Calculates the duration of the workout at the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/begincollection(withstart:completion:))*