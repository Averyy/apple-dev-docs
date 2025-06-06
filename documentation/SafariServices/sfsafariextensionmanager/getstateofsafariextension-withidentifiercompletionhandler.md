# getStateOfSafariExtension(withIdentifier:completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Gets the current state of the Safari app extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class func stateOfSafariExtension(withIdentifier identifier: String) async throws -> SFSafariExtensionState
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func stateOfSafariExtension(withIdentifier identifier: String) async throws -> SFSafariExtensionState
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func stateOfSafariExtension(withIdentifier identifier: String) async throws -> SFSafariExtensionState
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method is used by your app to check on the state of one of the Safari app extensions embedded inside it.

## Parameters

- `identifier`: The bundle identifier for the Safari extension to check.
- `completionHandler`: The completion handler the system calls with the Safari extension’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager/getstateofsafariextension(withidentifier:completionhandler:))*