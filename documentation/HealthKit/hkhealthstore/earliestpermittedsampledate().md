# earliestPermittedSampleDate()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Returns the earliest date that the framework permits your app to save or read samples.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func earliestPermittedSampleDate() -> Date
```

```objc
- (NSDate *) earliestPermittedSampleDate;
```

## Mentions

- [About the HealthKit framework](../about-the-healthkit-framework.md)

## Return Value

The earliest date that samples can use. HealthKit doesn’t allow saving or querying samples prior to this date.

## Discussion

Attempts to save samples earlier than this date fail with an [`HKError.Code.errorInvalidArgument`](../hkerror/code/errorinvalidargument.md) error. Attempts to query samples before this date return samples after this date.

This date is a systemwide platform constraint that applies equally to all apps. It isn’t related to what the person chooses to share with your app. To determine whether the person grants your app a limited portion of their health history, use [`getEarliestAuthorizedSampleDate(for:completion:)`](./getearliestauthorizedsampledate%28for,completion%29.md).

## See Also

### Accessing HealthKit
- [func authorizationStatus(for: HKObjectType) -> HKAuthorizationStatus](./authorizationstatus%28for%29.md)
  Returns the app’s authorization status for sharing the specified data type.
- [enum HKAuthorizationStatus](../hkauthorizationstatus.md)
  Constants indicating the authorization status for a particular data type.
- [func getRequestStatusForAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>, completion: (HKAuthorizationRequestStatus, (any Error)?) -> Void)](./getrequeststatusforauthorization%28toshare,read,completion%29.md)
  Indicates whether the system presents the user with a permission sheet if your app requests authorization for the provided types.
- [enum HKAuthorizationRequestStatus](../hkauthorizationrequeststatus.md)
  Values that indicate whether your app needs to request authorization from the user.
- [class func isHealthDataAvailable() -> Bool](./ishealthdataavailable%28%29.md)
  Returns a Boolean value that indicates whether HealthKit is available on this device.
- [func supportsHealthRecords() -> Bool](./supportshealthrecords%28%29.md)
  Returns a Boolean value that indicates whether the current device supports clinical records.
- [func requestAuthorization(toShare: Set<HKSampleType>?, read: Set<HKObjectType>?, completion: (Bool, (any Error)?) -> Void)](./requestauthorization%28toshare,read,completion%29.md)
  Requests permission to save and read the specified data types.
- [func requestAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>) async throws](./requestauthorization%28toshare,read%29.md)
  Asynchronously requests permission to save and read the specified data types.
- [func requestPerObjectReadAuthorization(for: HKObjectType, predicate: NSPredicate?, completion: (Bool, (any Error)?) -> Void)](./requestperobjectreadauthorization%28for,predicate,completion%29.md)
  Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [func handleAuthorizationForExtension(completion: (Bool, (any Error)?) -> Void)](./handleauthorizationforextension%28completion%29.md)
  Requests permission to save and read the data types specified by an extension.
- [var authorizationViewControllerPresenter: UIViewController?](./authorizationviewcontrollerpresenter.md)
  The view controller that presents HealthKit authorization sheets.
- [func getEarliestAuthorizedSampleDate(for: Set<HKObjectType>, completion: ([HKObjectType : Date]?, (any Error)?) -> Void)](./getearliestauthorizedsampledate%28for,completion%29.md)
  Returns the earliest date that the person permits your app to read samples for the given data types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/earliestpermittedsampledate())*