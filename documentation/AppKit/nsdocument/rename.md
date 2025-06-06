# rename(_:)

**Framework**: AppKit  
**Kind**: method

Renames the current document in response to the user choosing the Rename menu item.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
@MainActor func rename(_ sender: Any?)
```

#### Discussion

This is the action method of the Rename menu item in a document-based app. The default implementation of this method initiates a renaming session in a window created by the `[self windowForSheet]` message.

## Parameters

- `sender`: The control sending the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/rename(_:))*