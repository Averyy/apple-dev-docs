# HKError.Code.errorHealthDataUnavailable

**Framework**: HealthKit  
**Kind**: case

HealthKit accessed on an unsupported device, such as an iPad.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case errorHealthDataUnavailable
```

#### Discussion

Because iOS apps can run on devices that don’t support HealthKit (for example, on an iPad), always verify that the current device supports HealthKit by calling [`isHealthDataAvailable()`](hkhealthstore/ishealthdataavailable().md) before calling any other HealthKit methods. If HealthKit isn’t available on the device, other HealthKit methods fail with an [`errorHealthDataUnavailable`](hkerror/errorhealthdataunavailable.md) error.

## See Also

- [HKError.Code.errorHealthDataRestricted](hkerror/code/errorhealthdatarestricted.md)
  A Mobile Device Management (MDM) profile restricts the use of HealthKit on this device.
- [HKError.Code.errorInvalidArgument](hkerror/code/errorinvalidargument.md)
  The app passed an invalid argument to the HealthKit API.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkerror/code/errorhealthdataunavailable)*