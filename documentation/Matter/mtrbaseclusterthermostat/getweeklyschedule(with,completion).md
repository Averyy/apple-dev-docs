# getWeeklySchedule(with:completion:)

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
func getWeeklySchedule(with params: MTRThermostatClusterGetWeeklyScheduleParams, completion: @escaping @Sendable (MTRThermostatClusterGetWeeklyScheduleResponseParams?, (any Error)?) -> Void)
```

```swift
func weeklySchedule(with params: MTRThermostatClusterGetWeeklyScheduleParams) async throws -> MTRThermostatClusterGetWeeklyScheduleResponseParams
```

```objc
- (void) getWeeklyScheduleWithParams:(MTRThermostatClusterGetWeeklyScheduleParams *) params completion:(void (^)(MTRThermostatClusterGetWeeklyScheduleResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthermostat/getweeklyschedule(with:completion:))*