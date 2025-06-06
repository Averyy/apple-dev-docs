# refreshKeyboardUI()

**Framework**: BrowserEngineKit  
**Kind**: method

Tells the system to refresh the keyboard UI.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
func refreshKeyboardUI()
```

#### Discussion

This lightweight method refreshes the selection UI.  For example, this could be invoked in response to programmatic text selection changes, independent of text interaction gestures

## See Also

- [func editabilityChanged()](betextinteraction/editabilitychanged.md)
  Tells the system that the document’s editability status has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/refreshkeyboardui())*