# getWeekDaySchedule(with:expectedValues:expectedValueInterval:completion:)

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
func getWeekDaySchedule(with params: MTRDoorLockClusterGetWeekDayScheduleParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRDoorLockClusterGetWeekDayScheduleResponseParams?, (any Error)?) -> Void)
```

```swift
func weekDaySchedule(with params: MTRDoorLockClusterGetWeekDayScheduleParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRDoorLockClusterGetWeekDayScheduleResponseParams
```

```objc
- (void) getWeekDayScheduleWithParams:(MTRDoorLockClusterGetWeekDayScheduleParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRDoorLockClusterGetWeekDayScheduleResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdoorlock/getweekdayschedule(with:expectedvalues:expectedvalueinterval:completion:))*