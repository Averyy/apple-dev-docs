# getWeekDaySchedule(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func getWeekDaySchedule(with params: MTRDoorLockClusterGetWeekDayScheduleParams, completion: @escaping @Sendable (MTRDoorLockClusterGetWeekDayScheduleResponseParams?, (any Error)?) -> Void)
```

```swift
func weekDaySchedule(with params: MTRDoorLockClusterGetWeekDayScheduleParams) async throws -> MTRDoorLockClusterGetWeekDayScheduleResponseParams
```

```objc
- (void) getWeekDayScheduleWithParams:(MTRDoorLockClusterGetWeekDayScheduleParams *) params completion:(void (^)(MTRDoorLockClusterGetWeekDayScheduleResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdoorlock/getweekdayschedule(with:completion:))*