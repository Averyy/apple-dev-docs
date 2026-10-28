# modifyEnabledAlarms(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command ModifyEnabledAlarms

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func modifyEnabledAlarms(with params: MTRDishwasherAlarmClusterModifyEnabledAlarmsParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func modifyEnabledAlarms(with params: MTRDishwasherAlarmClusterModifyEnabledAlarmsParams) async throws
```

```objc
- (void) modifyEnabledAlarmsWithParams:(MTRDishwasherAlarmClusterModifyEnabledAlarmsParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

This command allows a client to request that an alarm be enabled or suppressed at the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdishwasheralarm/modifyenabledalarms(with:completion:))*