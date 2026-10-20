# HKError.Code.errorNoData

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

Data is unavailable for the requested query and predicate.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case errorNoData
```

```c
HKErrorNoData
```

#### Discussion

This error indicates that no data exists that corresponds to a particular query, so the system can’t calculate the query’s result. [`HKStatisticsQuery`](../../hkstatisticsquery.md) queries return this error when HealthKit can’t return the data needed to calculate the statistics.

## See Also

### Errors
- [HKError.Code.errorHealthDataUnavailable](./errorhealthdataunavailable.md)
  HealthKit accessed on an unsupported device, such as an iPad.
- [HKError.Code.errorHealthDataRestricted](./errorhealthdatarestricted.md)
  A Mobile Device Management (MDM) profile restricts the use of HealthKit on this device.
- [HKError.Code.errorInvalidArgument](./errorinvalidargument.md)
  The app passed an invalid argument to the HealthKit API.
- [HKError.Code.errorAuthorizationDenied](./errorauthorizationdenied.md)
  The user hasn’t given the app permission to save data.
- [HKError.Code.errorAuthorizationNotDetermined](./errorauthorizationnotdetermined.md)
  The app hasn’t yet asked the user for the authorization required to complete the task.
- [HKError.Code.errorRequiredAuthorizationDenied](./errorrequiredauthorizationdenied.md)
  The user hasn’t granted the application authorization to access all the required clinical record types.
- [HKError.Code.errorDatabaseInaccessible](./errordatabaseinaccessible.md)
  The HealthKit data is unavailable because it’s protected and the device is locked.
- [HKError.Code.errorUserCanceled](./errorusercanceled.md)
  The user canceled the operation.
- [HKError.Code.errorAnotherWorkoutSessionStarted](./erroranotherworkoutsessionstarted.md)
  Another app started a workout session.
- [HKError.Code.errorUserExitedWorkoutSession](./erroruserexitedworkoutsession.md)
  The user exited your application while a workout session was running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkerror/code/errornodata)*