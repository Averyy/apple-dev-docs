# openTab(with:makeActiveIfPossible:completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Opens a tab at the end of the tab bar.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func openTab(with url: URL, makeActiveIfPossible activateTab: Bool) async -> SFSafariTab?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func openTab(with url: URL, makeActiveIfPossible activateTab: Bool) async -> SFSafariTab?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

If the extension cannot access the URL, no tab is opened.

## Parameters

- `url`: The URL to navigate to.
- `activateTab`:   to make the tab active; otherwise  .
- `completionHandler`: A block called after the tab is opened.

## See Also

- [func getActiveTab(completionHandler: (SFSafariTab?) -> Void)](sfsafariwindow/getactivetab(completionhandler:).md)
  Calls the completion handler with the active tab in the target window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariwindow/opentab(with:makeactiveifpossible:completionhandler:))*