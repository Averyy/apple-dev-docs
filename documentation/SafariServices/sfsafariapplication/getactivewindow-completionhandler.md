# getActiveWindow(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Calls the completion handler with the active browser window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class func activeWindow() async -> SFSafariWindow?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func activeWindow() async -> SFSafariWindow?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

If there is no active Safari window, the value of `activeWindow` is `nil`, and the completion handler is not called.

## Parameters

- `completionHandler`: A block to call when the active browser window is returned.

## See Also

- [class func openWindow(with: URL, completionHandler: ((SFSafariWindow?) -> Void)?)](sfsafariapplication/openwindow(with:completionhandler:).md)
  Opens a new window with the desired webpage.
- [class func showPreferencesForExtension(withIdentifier: String, completionHandler: (((any Error)?) -> Void)?)](sfsafariapplication/showpreferencesforextension(withidentifier:completionhandler:).md)
  Launches Safari and opens the preferences panel for a Safari app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariapplication/getactivewindow(completionhandler:))*