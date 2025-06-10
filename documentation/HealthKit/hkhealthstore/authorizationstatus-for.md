# authorizationStatus(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the app’s authorization status for sharing the specified data type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func authorizationStatus(for type: HKObjectType) -> HKAuthorizationStatus
```

## Mentions

- [Authorizing access to health data](authorizing-access-to-health-data.md)

#### Return Value

A value indicating the app’s authorization status for this type. For a list of possible values, see [`HKAuthorizationStatus`](hkauthorizationstatus.md).

#### Discussion

This method checks the authorization status for saving data to the HealthKit store.

> ❗ **Important**:  An app’s permissions don’t change when an app runs in a Guest User session. Therefore, [`authorizationStatus(for:)`](hkhealthstore/authorizationstatus(for:).md) returns [`true`](https://developer.apple.com/documentation/swift/true) if the owner previously granted authorization to write the data, even though the app can’t write it during a Guest User session. For more information, refer to [`Authorizing access to health data`](authorizing-access-to-health-data.md).

To help prevent possible leaks of sensitive health information, your app cannot determine whether or not a user has granted permission to read data. If you are not given permission, it  simply appears as if there is no data of the requested type in the HealthKit store. If your app is given share permission but not read permission, you see only the data that your app has written to the store. Data from other sources remains hidden.

## Parameters

- `type`: The type of data. This can be any concrete subclass of the   class (any of the   ,  ,  ,   or   classes).

## See Also

- [enum HKAuthorizationStatus](hkauthorizationstatus.md)
  Constants indicating the authorization status for a particular data type.
- [func getRequestStatusForAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>, completion: (HKAuthorizationRequestStatus, (any Error)?) -> Void)](hkhealthstore/getrequeststatusforauthorization(toshare:read:completion:).md)
  Indicates whether the system presents the user with a permission sheet if your app requests authorization for the provided types.
- [enum HKAuthorizationRequestStatus](hkauthorizationrequeststatus.md)
  Values that indicate whether your app needs to request authorization from the user.
- [class func isHealthDataAvailable() -> Bool](hkhealthstore/ishealthdataavailable.md)
  Returns a Boolean value that indicates whether HealthKit is available on this device.
- [func supportsHealthRecords() -> Bool](hkhealthstore/supportshealthrecords.md)
  Returns a Boolean value that indicates whether the current device supports clinical records.
- [func requestAuthorization(toShare: Set<HKSampleType>?, read: Set<HKObjectType>?, completion: (Bool, (any Error)?) -> Void)](hkhealthstore/requestauthorization(toshare:read:completion:).md)
  Requests permission to save and read the specified data types.
- [func requestAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>) async throws](hkhealthstore/requestauthorization(toshare:read:).md)
  Asynchronously requests permission to save and read the specified data types.
- [func requestPerObjectReadAuthorization(for: HKObjectType, predicate: NSPredicate?, completion: (Bool, (any Error)?) -> Void)](hkhealthstore/requestperobjectreadauthorization(for:predicate:completion:).md)
  Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [func handleAuthorizationForExtension(completion: (Bool, (any Error)?) -> Void)](hkhealthstore/handleauthorizationforextension(completion:).md)
  Requests permission to save and read the data types specified by an extension.
- [var authorizationViewControllerPresenter: UIViewController?](hkhealthstore/authorizationviewcontrollerpresenter.md)
  The view controller that presents HealthKit authorization sheets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/authorizationstatus(for:))*