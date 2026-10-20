# getHolidaySchedule(with:completion:)

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
func getHolidaySchedule(with params: MTRDoorLockClusterGetHolidayScheduleParams, completion: @escaping @Sendable (MTRDoorLockClusterGetHolidayScheduleResponseParams?, (any Error)?) -> Void)
```

```swift
func holidaySchedule(with params: MTRDoorLockClusterGetHolidayScheduleParams) async throws -> MTRDoorLockClusterGetHolidayScheduleResponseParams
```

```objc
- (void) getHolidayScheduleWithParams:(MTRDoorLockClusterGetHolidayScheduleParams *) params completion:(void (^)(MTRDoorLockClusterGetHolidayScheduleResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdoorlock/getholidayschedule(with:completion:))*