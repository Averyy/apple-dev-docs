# authorizationViewControllerPresenter

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The view controller that presents HealthKit authorization sheets.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
weak var authorizationViewControllerPresenter: UIViewController? { get set }
```

```objc
@property (nonatomic, weak, nullable) UIViewController * authorizationViewControllerPresenter;
```

## Discussion

By default, the system infers the correct view controller to show HealthKit’s authorization sheet. In some cases, you can improve the user experience by explicitly defining how the system presents the authentication sheets. In particular, consider setting this property when using HealthKit in an iPadOS app.

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
- [func getEarliestAuthorizedSampleDate(for: Set<HKObjectType>, completion: ([HKObjectType : Date]?, (any Error)?) -> Void)](./getearliestauthorizedsampledate%28for,completion%29.md)
  Returns the earliest date that the person permits your app to read samples for the given data types.
- [func earliestPermittedSampleDate() -> Date](./earliestpermittedsampledate%28%29.md)
  Returns the earliest date that the framework permits your app to save or read samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/authorizationviewcontrollerpresenter)*