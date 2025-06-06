# getTestDiagnosisKeys(completionHandler:)

**Framework**: Exposure Notification  
**Kind**: method

Requests the temporary exposure keys, including the current key, used by this device for testing.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
func testDiagnosisKeys() async throws -> [ENTemporaryExposureKey]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func testDiagnosisKeys() async throws -> [ENTemporaryExposureKey]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func testDiagnosisKeys() async throws -> [ENTemporaryExposureKey]
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

> ❗ **Important**:  This method is available in iOS 12.5, and in iOS 13.5 and later.

 This method is available in iOS 12.5, and in iOS 13.5 and later.

Every time this method is called, the framework will request the user to authorize the action.

> ⚠️ **Warning**:  This method is only for developers while testing, and requires a special entitlement that is not allowed in the App Store. It’s only intended for testing without needing to wait 24 hours for a key to be released.

 This method is only for developers while testing, and requires a special entitlement that is not allowed in the App Store. It’s only intended for testing without needing to wait 24 hours for a key to be released.

## Parameters

- `completionHandler`: The completion handler that the framework calls when the method completes.

## See Also

- [func getDiagnosisKeys(completionHandler: ENGetDiagnosisKeysHandler)](enmanager/getdiagnosiskeys(completionhandler:).md)
  Requests the temporary exposure keys from the user’s device to share with a server.
- [class ENTemporaryExposureKey](entemporaryexposurekey.md)
  The key used to generate rolling proximity identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/gettestdiagnosiskeys(completionhandler:))*