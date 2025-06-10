# getActiveTab(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Calls the completion handler with the active tab in the target window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func activeTab() async -> SFSafariTab?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func activeTab() async -> SFSafariTab?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: A block called after the active tab is retrieved.

## See Also

- [func openTab(with: URL, makeActiveIfPossible: Bool, completionHandler: ((SFSafariTab?) -> Void)?)](sfsafariwindow/opentab(with:makeactiveifpossible:completionhandler:).md)
  Opens a tab at the end of the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariwindow/getactivetab(completionhandler:))*