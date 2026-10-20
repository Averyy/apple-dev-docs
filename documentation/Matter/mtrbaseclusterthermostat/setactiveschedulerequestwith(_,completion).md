# setActiveScheduleRequestWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetActiveScheduleRequest

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
func setActiveScheduleRequestWith(_ params: MTRThermostatClusterSetActiveScheduleRequestParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setActiveScheduleRequestWith(_ params: MTRThermostatClusterSetActiveScheduleRequestParams) async throws
```

```objc
- (void) setActiveScheduleRequestWithParams:(MTRThermostatClusterSetActiveScheduleRequestParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command will set the active schedule to the provided schedule handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthermostat/setactiveschedulerequestwith(_:completion:))*