# preAuthorizeDiagnosisKeys(completionHandler:)

**Framework**: Exposure Notification  
**Kind**: method  
**Role**: Instance Method

Allows users to authorize a one-time release of diagnosis keys within five days of the authorization.

**Availability**:
- iOS 14.4+ - Deprecated in 27.0
- iPadOS 14.4+ - Deprecated in 27.0
- Mac Catalyst 14.4+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
func preAuthorizeDiagnosisKeys(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func preAuthorizeDiagnosisKeys() async throws
```

```objc
- (void) preAuthorizeDiagnosisKeysWithCompletionHandler:(ENErrorHandler) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func preAuthorizeDiagnosisKeys() async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

> ❗ **Important**:  Before requesting authorization, ensure the application is in the foreground.

This method prompts the user when getting tested to share their diagnosis keys if they receive a positive test result. An app should only call this method if it has a way to determine that the user is about to take a COVID test, such as apps that allow users to schedule testing appointments, and that can also determine if the result is positive.

The authorization duration is five days.

## Parameters

- `completionHandler`: The completion handler the framework calls when the method completes.

## See Also

### Preauthorizing Exposure Keys
- [func requestPreAuthorizedDiagnosisKeys(completionHandler: ((any Error)?) -> Void)](./requestpreauthorizeddiagnosiskeys%28completionhandler%29.md)
  Requests diagnosis keys after the user authorizes sharing them.
- [typealias ENDiagnosisKeysAvailableHandler](../endiagnosiskeysavailablehandler.md)
  The handler the system invokes after requesting diagnosis keys.
- [var diagnosisKeysAvailableHandler: ENDiagnosisKeysAvailableHandler?](./diagnosiskeysavailablehandler.md)
  The handler that receives available diagnosis keys after a successful preauthorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/preauthorizediagnosiskeys(completionhandler:))*