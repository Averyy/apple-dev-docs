# HKError.Code.errorHealthDataUnavailable

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

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

```c
HKErrorHealthDataUnavailable
```

## Discussion

Because iOS apps can run on devices that don’t support HealthKit (for example, on an iPad), always verify that the current device supports HealthKit by calling [`isHealthDataAvailable()`](../../hkhealthstore/ishealthdataavailable%28%29.md) before calling any other HealthKit methods. If HealthKit isn’t available on the device, other HealthKit methods fail with an [`errorHealthDataUnavailable`](../errorhealthdataunavailable.md) error.

## See Also

### Errors
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
- [HKError.Code.errorNoData](./errornodata.md)
  Data is unavailable for the requested query and predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkerror/code/errorhealthdataunavailable)*