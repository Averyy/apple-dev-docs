# setActiveScheduleRequestWith(_:completion:)

**Framework**: Matter  
**Kind**: method

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
func setActiveScheduleRequestWith(_ params: MTRThermostatClusterSetActiveScheduleRequestParams) async throws
```

#### Discussion

Upon receipt, if the Schedules attribute contains a ScheduleStruct whose ScheduleHandle field matches the value of the ScheduleHandle field, the server SHALL set the thermostat’s ActiveScheduleHandle attribute to the value of the ScheduleHandle field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthermostat/setactiveschedulerequestwith(_:completion:))*