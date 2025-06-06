# HKError.Code.errorInvalidArgument

**Framework**: HealthKit  
**Kind**: case

The app passed an invalid argument to the HealthKit API.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case errorInvalidArgument
```

## See Also

- [HKError.Code.errorHealthDataUnavailable](hkerror/code/errorhealthdataunavailable.md)
  HealthKit accessed on an unsupported device, such as an iPad.
- [HKError.Code.errorHealthDataRestricted](hkerror/code/errorhealthdatarestricted.md)
  A Mobile Device Management (MDM) profile restricts the use of HealthKit on this device.
- [HKError.Code.errorAuthorizationDenied](hkerror/code/errorauthorizationdenied.md)
  The user hasn’t given the app permission to save data.
- [HKError.Code.errorAuthorizationNotDetermined](hkerror/code/errorauthorizationnotdetermined.md)
  The app hasn’t yet asked the user for the authorization required to complete the task.
- [HKError.Code.errorRequiredAuthorizationDenied](hkerror/code/errorrequiredauthorizationdenied.md)
  The user hasn’t granted the application authorization to access all the required clinical record types.
- [HKError.Code.errorDatabaseInaccessible](hkerror/code/errordatabaseinaccessible.md)
  The HealthKit data is unavailable because it’s protected and the device is locked.
- [HKError.Code.errorUserCanceled](hkerror/code/errorusercanceled.md)
  The user canceled the operation.
- [HKError.Code.errorAnotherWorkoutSessionStarted](hkerror/code/erroranotherworkoutsessionstarted.md)
  Another app started a workout session.
- [HKError.Code.errorUserExitedWorkoutSession](hkerror/code/erroruserexitedworkoutsession.md)
  The user exited your application while a workout session was running.
- [HKError.Code.errorNoData](hkerror/code/errornodata.md)
  Data is unavailable for the requested query and predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkerror/code/errorinvalidargument)*