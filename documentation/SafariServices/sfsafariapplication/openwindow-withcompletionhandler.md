# openWindow(with:completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Opens a new window with the desired webpage.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class func openWindow(with url: URL) async -> SFSafariWindow?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func openWindow(with url: URL) async -> SFSafariWindow?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func openWindow(with url: URL) async -> SFSafariWindow?
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `url`: The URL to navigate to. The URL scheme must be   or  .
- `completionHandler`: A block to call when the URL is loaded in a new window.

## See Also

- [class func getActiveWindow(completionHandler: (SFSafariWindow?) -> Void)](sfsafariapplication/getactivewindow(completionhandler:).md)
  Calls the completion handler with the active browser window.
- [class func showPreferencesForExtension(withIdentifier: String, completionHandler: (((any Error)?) -> Void)?)](sfsafariapplication/showpreferencesforextension(withidentifier:completionhandler:).md)
  Launches Safari and opens the preferences panel for a Safari app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariapplication/openwindow(with:completionhandler:))*