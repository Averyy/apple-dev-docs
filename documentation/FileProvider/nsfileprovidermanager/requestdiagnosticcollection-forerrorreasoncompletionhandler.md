# requestDiagnosticCollection(for:errorReason:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Requests a diagnostics collection for use when working directly with Apple to improve sync behavior.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func requestDiagnosticCollection(for itemIdentifier: NSFileProviderItemIdentifier, errorReason: any Error) async throws
```

#### Discussion

Calling this method requests that the system prompt the person using the app, who may be experiencing an issue with sync in your provider. It asks their permission to collect and send diagnostic information to Apple for further analysis. Even if the person gives their approval, however, the prompt or the diagnostic collection might not occur, depending on system state and other throttling parameters.

When calling this method, use the `errorReason` parameter to describe the error that prompted the request for diagnostics. The system doesn’t show this error to the person using the app. Instead, the error appears in any generated reports created from the diagnostics.

The system may or may not allow the request, and the method call returns normally in either case. It produces an error — thrown in Swift and sent to the completion handler in Objective-C — if any of the following occur:

- The app isn’t running on a pre-release build.
- The app is running on a pre-release build, but the system can’t find the item indicated by the `itemIdentifier` parameter.

> ❗ **Important**: Only use this call in collaboration with Apple when working to resolve possible system bugs in sync behavior. The system throttles calls to this method to prevent inconveniencing people using your app.

Only use this call in collaboration with Apple when working to resolve possible system bugs in sync behavior. The system throttles calls to this method to prevent inconveniencing people using your app.

## Parameters

- `itemIdentifier`: The item that failed to sync.
- `errorReason`: An error instance that indicates why the sync failed. If you use a Swift  , the system coerces it to an   and uses only the domain and code.
- `completionHandler`: A block or closure that executes after the system processes the diagnostic collection request. The completion handler receives an error parameter, which is non-  if an error prevented collection of diagnostics. In Swift, you can omit the completion handler and instead use a  -  block to handle the thrown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/requestdiagnosticcollection(for:errorreason:completionhandler:))*