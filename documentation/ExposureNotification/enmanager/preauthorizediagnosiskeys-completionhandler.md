# preAuthorizeDiagnosisKeys(completionHandler:)

**Framework**: Exposure Notification  
**Kind**: method

Allows users to authorize a one-time release of diagnosis keys within five days of the authorization.

**Availability**:
- iOS 14.4+
- iPadOS 14.4+
- Mac Catalyst 14.4+

## Declaration

```swift
func preAuthorizeDiagnosisKeys() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func preAuthorizeDiagnosisKeys() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

> ❗ **Important**:  Before requesting authorization, ensure the application is in the foreground.

This method prompts the user when getting tested to share their diagnosis keys if they receive a positive test result. An app should only call this method if it has a way to determine that the user is about to take a COVID test, such as apps that allow users to schedule testing appointments, and that can also determine if the result is positive.

The authorization duration is five days.

## Parameters

- `completionHandler`: The completion handler the framework calls when the method completes.

## See Also

- [func requestPreAuthorizedDiagnosisKeys(completionHandler: ((any Error)?) -> Void)](enmanager/requestpreauthorizeddiagnosiskeys(completionhandler:).md)
  Requests diagnosis keys after the user authorizes sharing them.
- [typealias ENDiagnosisKeysAvailableHandler](endiagnosiskeysavailablehandler.md)
  The handler the system invokes after requesting diagnosis keys.
- [var diagnosisKeysAvailableHandler: ENDiagnosisKeysAvailableHandler?](enmanager/diagnosiskeysavailablehandler.md)
  The handler that receives available diagnosis keys after a successful preauthorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/preauthorizediagnosiskeys(completionhandler:))*