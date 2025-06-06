# requestAuthorization(toShare:read:)

**Framework**: HealthKit  
**Kind**: method

Asynchronously requests permission to save and read the specified data types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func requestAuthorization(toShare typesToShare: Set<HKSampleType>, read typesToRead: Set<HKObjectType>) async throws
```

## Mentions

- [Authorizing access to health data](authorizing-access-to-health-data.md)

#### Discussion

HealthKit performs these requests asynchronously. If you call this method with a new data type (a type of data that the user hasn’t previously granted or denied permission for in this app), the system automatically displays the permission form, listing all the requested permissions. If the user has already chosen to grant or prohibit access to all of the types specified, HealthKit returns the request without prompting the user.

> ❗ **Important**:  In watchOS 6 and later, this method displays the permission form on Apple Watch, enabling independent HealthKit apps. In watchOS 5 and earlier, this method prompts the user to authorize the app on their paired iPhone. For more information, see `Creating Independent watchOS Apps`.

 In watchOS 6 and later, this method displays the permission form on Apple Watch, enabling independent HealthKit apps. In watchOS 5 and earlier, this method prompts the user to authorize the app on their paired iPhone. For more information, see `Creating Independent watchOS Apps`.

Each data type has two separate permissions, one to read it and one to share it. You can make a single request, and include all the data types your app needs.

Customize the messages displayed on the permissions sheet by setting the following keys:

- [`NSHealthShareUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHealthShareUsageDescription) customizes the message for reading data.
- [`NSHealthUpdateUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHealthUpdateUsageDescription) customizes the message for writing data.

> ⚠️ **Warning**:  You must set the usage keys, or your app will crash when you request authorization.

 You must set the usage keys, or your app will crash when you request authorization.

For projects created using Xcode 13 or later, set these keys in the Target Properties list on the app’s Info tab. For projects created with Xcode 12 or earlier, set these keys in the apps `Info.plist` file. For more information, see [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List).

After users have set the permissions for your app, they can always change them using either the Settings or the Health app. Your app appears in the Health app’s Sources tab, even if the user didn’t allow permission to read or share data.

## Parameters

- `typesToShare`: A set containing the data types you want to share. This set can contain any concrete subclass of the   class (any of the  ,  ,  , or   classes). If the user grants permission, your app can create and save these data types to the HealthKit store.
- `typesToRead`: A set containing the data types you want to read. This set can contain any concrete subclass of the   class (any of the   ,  ,  ,  , or   classes ). If the user grants permission, your app can read these data types from the HealthKit store.

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
- [func requestPerObjectReadAuthorization(for: HKObjectType, predicate: NSPredicate?, completion: (Bool, (any Error)?) -> Void)](hkhealthstore/requestperobjectreadauthorization(for:predicate:completion:).md)
  Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [func handleAuthorizationForExtension(completion: (Bool, (any Error)?) -> Void)](hkhealthstore/handleauthorizationforextension(completion:).md)
  Requests permission to save and read the data types specified by an extension.
- [var authorizationViewControllerPresenter: UIViewController?](hkhealthstore/authorizationviewcontrollerpresenter.md)
  The view controller that presents HealthKit authorization sheets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/requestauthorization(toshare:read:))*