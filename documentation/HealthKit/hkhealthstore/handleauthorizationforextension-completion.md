# handleAuthorizationForExtension(completion:)

**Framework**: HealthKit  
**Kind**: method

Requests permission to save and read the data types specified by an extension.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func handleAuthorizationForExtension() async throws
```

#### Discussion

The host app must implement the application delegate’s [`applicationShouldRequestHealthAuthorization(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationShouldRequestHealthAuthorization(_:)) method. This delegate method is called after an app extension calls [`requestAuthorization(toShare:read:completion:)`](hkhealthstore/requestauthorization(toshare:read:completion:).md). The host app is then responsible for calling [`handleAuthorizationForExtension(completion:)`](hkhealthstore/handleauthorizationforextension(completion:).md). This method prompts the user to authorize both the app and its extensions for the types that the extension requested.

The system performs this request asynchronously. After the user has finished responding, this method calls its completion block on a background queue. If the user has already chosen to grant or prohibit access to all of the types specified, the completion is called without prompting the user.

## Parameters

- `completion`: A block that is called after the user finishes responding to the request. This block is passed the following parameters:

## See Also

- [func authorizationStatus(for: HKObjectType) -> HKAuthorizationStatus](hkhealthstore/authorizationstatus(for:).md)
  Returns the app’s authorization status for sharing the specified data type.
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
- [var authorizationViewControllerPresenter: UIViewController?](hkhealthstore/authorizationviewcontrollerpresenter.md)
  The view controller that presents HealthKit authorization sheets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/handleauthorizationforextension(completion:))*