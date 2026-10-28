# errorHealthDataUnavailable

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

The user accessed HealthKit on an unsupported device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var errorHealthDataUnavailable: HKError.Code { get }
```

## Discussion

Because iOS apps can run on devices that don’t support HealthKit (for example, on an iPad), always verify that the current device supports HealthKit by calling [`isHealthDataAvailable()`](../hkhealthstore/ishealthdataavailable%28%29.md) before calling any other HealthKit methods. If HealthKit isn’t available on the device, other HealthKit methods fail with an [`errorHealthDataUnavailable`](./errorhealthdataunavailable.md) error.

## See Also

### Accessing errors
- [HKError.Code](./code.md)
  Error codes returned by HealthKit.
- [static var noError: HKError.Code](./noerror.md)
  No error occurred.
- [static var errorHealthDataRestricted: HKError.Code](./errorhealthdatarestricted.md)
  A Mobile Device Management (MDM) profile restricts the use of HealthKit on this device.
- [static var errorInvalidArgument: HKError.Code](./errorinvalidargument.md)
  The app passed an invalid argument to the HealthKit API.
- [static var errorAuthorizationDenied: HKError.Code](./errorauthorizationdenied.md)
  The user hasn’t given the app permission to save data.
- [static var errorAuthorizationNotDetermined: HKError.Code](./errorauthorizationnotdetermined.md)
  The app hasn’t yet asked the user for the authorization required to complete the task.
- [static var errorRequiredAuthorizationDenied: HKError.Code](./errorrequiredauthorizationdenied.md)
  The user hasn’t granted the application authorization to access all the required clinical record types.
- [static var errorDatabaseInaccessible: HKError.Code](./errordatabaseinaccessible.md)
  The HealthKit data is unavailable because it’s protected and the device is locked.
- [static var errorUserCanceled: HKError.Code](./errorusercanceled.md)
  The user canceled the operation.
- [static var errorAnotherWorkoutSessionStarted: HKError.Code](./erroranotherworkoutsessionstarted.md)
  Another app started a workout session.
- [static var errorUserExitedWorkoutSession: HKError.Code](./erroruserexitedworkoutsession.md)
  The user exited your application while a workout session was running.
- [static var errorNoData: HKError.Code](./errornodata.md)
  Data is unavailable for the requested query and predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkerror/errorhealthdataunavailable)*