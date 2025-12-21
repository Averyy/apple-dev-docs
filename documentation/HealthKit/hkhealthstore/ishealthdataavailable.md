# isHealthDataAvailable()

**Framework**: HealthKit  
**Kind**: method

Returns a Boolean value that indicates whether HealthKit is available on this device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func isHealthDataAvailable() -> Bool
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)
- [Authorizing access to health data](authorizing-access-to-health-data.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if HealthKit is available; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

By default, HealthKit data is available on iOS, watchOS, and visionOS. HealthKit data is also available to iPads running iPadOS 17 or later, and to iOS apps running on Vision Pro. Devices running in an enterprise environment may restrict access to HealthKit data.

The HealthKit framework is available on devices running iPadOS 16 and earlier and macOS 13 and later, but your app can’t read or write HealthKit data. Calls to [`isHealthDataAvailable()`](hkhealthstore/ishealthdataavailable().md) return [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func authorizationStatus(for: HKObjectType) -> HKAuthorizationStatus](hkhealthstore/authorizationstatus(for:).md)
  Returns the app’s authorization status for sharing the specified data type.
- [enum HKAuthorizationStatus](hkauthorizationstatus.md)
  Constants indicating the authorization status for a particular data type.
- [func getRequestStatusForAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>, completion: (HKAuthorizationRequestStatus, (any Error)?) -> Void)](hkhealthstore/getrequeststatusforauthorization(toshare:read:completion:).md)
  Indicates whether the system presents the user with a permission sheet if your app requests authorization for the provided types.
- [enum HKAuthorizationRequestStatus](hkauthorizationrequeststatus.md)
  Values that indicate whether your app needs to request authorization from the user.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/ishealthdataavailable())*