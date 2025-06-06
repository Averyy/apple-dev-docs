# performTextFinderAction(_:)

**Framework**: AppKit  
**Kind**: method

Performs all find oriented actions.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func performTextFinderAction(_ sender: Any?)
```

#### Discussion

When an application performs a find action, it should send this message to the responder chain.

A responder of `performTextFinderAction:` is responsible for creating and owning an instance of `NSTextFinder`. Before any other messages are sent to the `NSTextFinder`, you should set its ‘client’ property to an object which implements the `NSTextFinderClient` protocol.

> **Note**:  Before OS X v10.7, the default action for these menu items was [`performFindPanelAction(_:)`](nstextview/performfindpanelaction(_:).md). Whenever possible which you should update your implementation to use this new action.

 Before OS X v10.7, the default action for these menu items was [`performFindPanelAction(_:)`](nstextview/performfindpanelaction(_:).md). Whenever possible which you should update your implementation to use this new action.

## Parameters

- `sender`: The sender of the find action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/performtextfinderaction(_:))*