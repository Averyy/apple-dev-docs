# selectText(_:)

**Framework**: AppKit  
**Kind**: method

Ends editing in the text field and, if it’s selectable, selects the entire text content.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectText(_ sender: Any?)
```

#### Discussion

If the text field isn’t in a window’s view hierarchy, this method has no effect.

## Parameters

- `sender`: The sender of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/selecttext(_:))*