# showPreferencesForExtension(withIdentifier:completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Launches Safari and opens the preferences panel for a Safari app extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class func showPreferencesForExtension(withIdentifier identifier: String) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func showPreferencesForExtension(withIdentifier identifier: String) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func showPreferencesForExtension(withIdentifier identifier: String) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `identifier`: The identifier for a Safari app extension in your app bundle.
- `completionHandler`: A completion handler called after the operation completes. The completion handler takes the following parameter:

## See Also

- [class func getActiveWindow(completionHandler: (SFSafariWindow?) -> Void)](sfsafariapplication/getactivewindow(completionhandler:).md)
  Calls the completion handler with the active browser window.
- [class func openWindow(with: URL, completionHandler: ((SFSafariWindow?) -> Void)?)](sfsafariapplication/openwindow(with:completionhandler:).md)
  Opens a new window with the desired webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariapplication/showpreferencesforextension(withidentifier:completionhandler:))*