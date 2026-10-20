# getWeekDaySchedule(with:expectedValues:expectedValueInterval:completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use getWeekDayScheduleWithParams:expectedValues:expectedValueInterval:completion:

## Declaration

```swift
func getWeekDaySchedule(with params: MTRDoorLockClusterGetWeekDayScheduleParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completionHandler: @escaping @Sendable (MTRDoorLockClusterGetWeekDayScheduleResponseParams?, (any Error)?) -> Void)
```

```swift
func weekDaySchedule(with params: MTRDoorLockClusterGetWeekDayScheduleParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRDoorLockClusterGetWeekDayScheduleResponseParams
```

```objc
- (void) getWeekDayScheduleWithParams:(MTRDoorLockClusterGetWeekDayScheduleParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completionHandler:(void (^)(MTRDoorLockClusterGetWeekDayScheduleResponseParams *data, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdoorlock/getweekdayschedule(with:expectedvalues:expectedvalueinterval:completionhandler:))*