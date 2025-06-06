# requestPreAuthorizedDiagnosisKeys(completionHandler:)

**Framework**: Exposure Notification  
**Kind**: method

Requests diagnosis keys after the user authorizes sharing them.

**Availability**:
- iOS 14.4+
- iPadOS 14.4+
- Mac Catalyst 14.4+

## Declaration

```swift
func requestPreAuthorizedDiagnosisKeys() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func requestPreAuthorizedDiagnosisKeys() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func requestPreAuthorizedDiagnosisKeys() async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

If the user authorizes sharing of diagnosis keys and receives a positive test result within five days, call this method to retrieve the preauthorized keys, but only after informing the user of the positive result. [`ENDiagnosisKeysAvailableHandler`](endiagnosiskeysavailablehandler.md) receives the keys when the user unlocks their device. Subsequent calls to this method have no effect. If more than five days pass after the user authorizes sharing of their keys, or if the user declines to share their keys, the completion handler returns an error.

> ❗ **Important**:  Your app must notify a user when their diagnosis keys are shared. The language of the notification must remind the user that they authorized the sharing of their diagnosis keys.  For example: “In accordance with your prior decision to share your keys if your test result was positive, your keys are now being shared with .”

 Your app must notify a user when their diagnosis keys are shared. The language of the notification must remind the user that they authorized the sharing of their diagnosis keys.  For example: “In accordance with your prior decision to share your keys if your test result was positive, your keys are now being shared with .”

## Parameters

- `completionHandler`: The completion handler the framework calls when the method completes.

## See Also

- [func preAuthorizeDiagnosisKeys(completionHandler: ENErrorHandler)](enmanager/preauthorizediagnosiskeys(completionhandler:).md)
  Allows users to authorize a one-time release of diagnosis keys within five days of the authorization.
- [typealias ENDiagnosisKeysAvailableHandler](endiagnosiskeysavailablehandler.md)
  The handler the system invokes after requesting diagnosis keys.
- [var diagnosisKeysAvailableHandler: ENDiagnosisKeysAvailableHandler?](enmanager/diagnosiskeysavailablehandler.md)
  The handler that receives available diagnosis keys after a successful preauthorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/requestpreauthorizeddiagnosiskeys(completionhandler:))*