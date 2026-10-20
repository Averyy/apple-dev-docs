# getYearDaySchedule(with:expectedValues:expectedValueInterval:completion:)

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
func getYearDaySchedule(with params: MTRDoorLockClusterGetYearDayScheduleParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRDoorLockClusterGetYearDayScheduleResponseParams?, (any Error)?) -> Void)
```

```swift
func yearDaySchedule(with params: MTRDoorLockClusterGetYearDayScheduleParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRDoorLockClusterGetYearDayScheduleResponseParams
```

```objc
- (void) getYearDayScheduleWithParams:(MTRDoorLockClusterGetYearDayScheduleParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRDoorLockClusterGetYearDayScheduleResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdoorlock/getyeardayschedule(with:expectedvalues:expectedvalueinterval:completion:))*