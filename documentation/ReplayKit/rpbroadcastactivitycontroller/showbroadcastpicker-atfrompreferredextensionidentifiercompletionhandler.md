# showBroadcastPicker(at:from:preferredExtensionIdentifier:completionHandler:)

**Framework**: ReplayKit  
**Kind**: method

Presents a list of available broadcast services for the user to select.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class func showBroadcastPicker(at point: CGPoint, from window: NSWindow?, preferredExtensionIdentifier preferredExtension: String?) async throws -> RPBroadcastActivityController
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func showBroadcastPicker(at point: CGPoint, from window: NSWindow?, preferredExtensionIdentifier preferredExtension: String?) async throws -> RPBroadcastActivityController
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `point`: The origin point within the specified window.
- `window`: The window presenting the picker. Specify   to present the picker from the main app window.
- `preferredExtension`: The extension bundle identifier for the preferred broadcast extension service. Specify   to show all extensions.
- `handler`: The system calls this closure after the user selects a broadcast extension. The system passes the closure the selected broadcast activity controller, or an error if a failure occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontroller/showbroadcastpicker(at:from:preferredextensionidentifier:completionhandler:))*