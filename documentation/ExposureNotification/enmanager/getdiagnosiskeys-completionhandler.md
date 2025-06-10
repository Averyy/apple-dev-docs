# getDiagnosisKeys(completionHandler:)

**Framework**: Exposure Notification  
**Kind**: method

Requests the temporary exposure keys from the user’s device to share with a server.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
func diagnosisKeys() async throws -> [ENTemporaryExposureKey]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func diagnosisKeys() async throws -> [ENTemporaryExposureKey]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

> ❗ **Important**:  This method is available in iOS 12.5, and in iOS 13.5 and later.

The app must be in the foreground when it calls this method. Each time the app calls this method, the system presents an interface that requests authorization.

When [`ENAPIVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ENAPIVersion) is set to `1` in the app’s Info.plist file, you must wait approximately 24 hours after the first call of [`getDiagnosisKeys(completionHandler:)`](enmanager/getdiagnosiskeys(completionhandler:).md) before this call returns a valid key. To test your app without waiting 24 hours, use [`getTestDiagnosisKeys(completionHandler:)`](enmanager/gettestdiagnosiskeys(completionhandler:).md).

When [`ENAPIVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ENAPIVersion) is set to `2`, this call returns a diagnosis key with a shortened rolling period.

## Parameters

- `completionHandler`: The completion handler that the framework calls when   completes. If the method completes successfully,   will contain the diagnosis keys for this device and   will be  . If it fails,   will be   and   indicates the reason it failed.

## Topics

### Completion Handlers
- [typealias ENGetDiagnosisKeysHandler](engetdiagnosiskeyshandler.md)
  The definition of a handler that returns diagnosis keys.

## See Also

- [func getTestDiagnosisKeys(completionHandler: ([ENTemporaryExposureKey]?, (any Error)?) -> Void)](enmanager/gettestdiagnosiskeys(completionhandler:).md)
  Requests the temporary exposure keys, including the current key, used by this device for testing.
- [class ENTemporaryExposureKey](entemporaryexposurekey.md)
  The key used to generate rolling proximity identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/getdiagnosiskeys(completionhandler:))*