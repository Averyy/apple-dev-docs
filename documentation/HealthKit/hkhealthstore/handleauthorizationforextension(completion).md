# handleAuthorizationForExtension(completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Requests permission to save and read the data types specified by an extension.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func handleAuthorizationForExtension(completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func handleAuthorizationForExtension() async throws
```

```objc
- (void) handleAuthorizationForExtensionWithCompletion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

The host app must implement the application delegate’s [`applicationShouldRequestHealthAuthorization(_:)`](../../UIKit/uiapplicationdelegate/applicationshouldrequesthealthauthorization%28_%29.md) method. This delegate method is called after an app extension calls [`requestAuthorization(toShare:read:completion:)`](./requestauthorization%28toshare,read,completion%29.md). The host app is then responsible for calling [`handleAuthorizationForExtension(completion:)`](./handleauthorizationforextension%28completion%29.md). This method prompts the user to authorize both the app and its extensions for the types that the extension requested.

The system performs this request asynchronously. After the user has finished responding, this method calls its completion block on a background queue. If the user has already chosen to grant or prohibit access to all of the types specified, the completion is called without prompting the user.

## Parameters

- `completion`: A block that is called after the user finishes responding to the request. This block is passed the following parameters:

  - **success**: A Boolean value that indicates whether the user responded to the prompt (if any). This value does not indicate whether permission was actually granted. This parameter is [`false`](../../Swift/false.md) if the user canceled the prompt without selecting permissions; otherwise, [`true`](../../Swift/true.md).
  - **error**: An error object. If an error occurred, this object contains information about the error; otherwise, it is set to `nil`.

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
- [var authorizationViewControllerPresenter: UIViewController?](./authorizationviewcontrollerpresenter.md)
  The view controller that presents HealthKit authorization sheets.
- [func getEarliestAuthorizedSampleDate(for: Set<HKObjectType>, completion: ([HKObjectType : Date]?, (any Error)?) -> Void)](./getearliestauthorizedsampledate%28for,completion%29.md)
  Returns the earliest date that the person permits your app to read samples for the given data types.
- [func earliestPermittedSampleDate() -> Date](./earliestpermittedsampledate%28%29.md)
  Returns the earliest date that the framework permits your app to save or read samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/handleauthorizationforextension(completion:))*