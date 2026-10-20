# beginCollection(withStart:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Sets the workout’s start date and begins building the workout.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func beginCollection(withStart startDate: Date, completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func beginCollection(at startDate: Date) async throws
```

```objc
- (void) beginCollectionWithStartDate:(NSDate *) startDate completion:(void (^)(BOOL success, NSError *error)) completion;
```

## See Also

### Starting the workout
- [var startDate: Date?](./startdate.md)
  The workout’s start date and time.
- [func elapsedTime(at: Date) -> TimeInterval](./elapsedtime%28at%29.md)
  Calculates the duration of the workout at the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/begincollection(withstart:completion:))*