# HKError.Code

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

Error codes returned by HealthKit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum Code
```

```c
enum HKErrorCode : NSInteger;
```

## Mentions

- [Executing Statistics Collection Queries](../executing-statistics-collection-queries.md)

## Topics

### Errors
- [HKError.Code.errorHealthDataUnavailable](./code/errorhealthdataunavailable.md)
  HealthKit accessed on an unsupported device, such as an iPad.
- [HKError.Code.errorHealthDataRestricted](./code/errorhealthdatarestricted.md)
  A Mobile Device Management (MDM) profile restricts the use of HealthKit on this device.
- [HKError.Code.errorInvalidArgument](./code/errorinvalidargument.md)
  The app passed an invalid argument to the HealthKit API.
- [HKError.Code.errorAuthorizationDenied](./code/errorauthorizationdenied.md)
  The user hasn’t given the app permission to save data.
- [HKError.Code.errorAuthorizationNotDetermined](./code/errorauthorizationnotdetermined.md)
  The app hasn’t yet asked the user for the authorization required to complete the task.
- [HKError.Code.errorRequiredAuthorizationDenied](./code/errorrequiredauthorizationdenied.md)
  The user hasn’t granted the application authorization to access all the required clinical record types.
- [HKError.Code.errorDatabaseInaccessible](./code/errordatabaseinaccessible.md)
  The HealthKit data is unavailable because it’s protected and the device is locked.
- [HKError.Code.errorUserCanceled](./code/errorusercanceled.md)
  The user canceled the operation.
- [HKError.Code.errorAnotherWorkoutSessionStarted](./code/erroranotherworkoutsessionstarted.md)
  Another app started a workout session.
- [HKError.Code.errorUserExitedWorkoutSession](./code/erroruserexitedworkoutsession.md)
  The user exited your application while a workout session was running.
- [HKError.Code.errorNoData](./code/errornodata.md)
  Data is unavailable for the requested query and predicate.
### Enumeration Cases
- [HKError.Code.errorBackgroundWorkoutSessionNotAllowed](./code/errorbackgroundworkoutsessionnotallowed.md)
- [HKError.Code.errorDataSizeExceeded](./code/errordatasizeexceeded.md)
- [HKError.Code.errorNotPermissibleForGuestUserMode](./code/errornotpermissibleforguestusermode.md)
  The app attempted to write HealthKit data while in a Guest User session in visionOS.
- [HKError.Code.errorWorkoutActivityNotAllowed](./code/errorworkoutactivitynotallowed.md)
- [HKError.Code.unknownError](./code/unknownerror.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)
### Type Properties
- [static var noError: HKError.Code](./code/noerror.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct HKError](../hkerror.md)
  An error returned from a HealthKit method.
- [let HKErrorDomain: String](../hkerrordomain.md)
  The domain for all HealthKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkerror/code)*