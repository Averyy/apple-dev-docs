# errorUserExitedWorkoutSession

**Framework**: HealthKit  
**Kind**: property

The user exited your application while a workout session was running.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var errorUserExitedWorkoutSession: HKError.Code { get }
```

#### Discussion

Workout sessions end when the app goes into the background.

## See Also

- [HKError.Code](hkerror/code.md)
  Error codes returned by HealthKit.
- [static var noError: HKError.Code](hkerror/noerror.md)
  No error occurred.
- [static var errorHealthDataUnavailable: HKError.Code](hkerror/errorhealthdataunavailable.md)
  The user accessed HealthKit on an unsupported device.
- [static var errorHealthDataRestricted: HKError.Code](hkerror/errorhealthdatarestricted.md)
  A Mobile Device Management (MDM) profile restricts the use of HealthKit on this device.
- [static var errorInvalidArgument: HKError.Code](hkerror/errorinvalidargument.md)
  The app passed an invalid argument to the HealthKit API.
- [static var errorAuthorizationDenied: HKError.Code](hkerror/errorauthorizationdenied.md)
  The user hasn’t given the app permission to save data.
- [static var errorAuthorizationNotDetermined: HKError.Code](hkerror/errorauthorizationnotdetermined.md)
  The app hasn’t yet asked the user for the authorization required to complete the task.
- [static var errorRequiredAuthorizationDenied: HKError.Code](hkerror/errorrequiredauthorizationdenied.md)
  The user hasn’t granted the application authorization to access all the required clinical record types.
- [static var errorDatabaseInaccessible: HKError.Code](hkerror/errordatabaseinaccessible.md)
  The HealthKit data is unavailable because it’s protected and the device is locked.
- [static var errorUserCanceled: HKError.Code](hkerror/errorusercanceled.md)
  The user canceled the operation.
- [static var errorAnotherWorkoutSessionStarted: HKError.Code](hkerror/erroranotherworkoutsessionstarted.md)
  Another app started a workout session.
- [static var errorNoData: HKError.Code](hkerror/errornodata.md)
  Data is unavailable for the requested query and predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkerror/erroruserexitedworkoutsession)*