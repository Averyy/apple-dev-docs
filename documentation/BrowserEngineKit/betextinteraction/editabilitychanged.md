# editabilityChanged()

**Framework**: BrowserEngineKit  
**Kind**: method

Tells the system that the document’s editability status has changed.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
func editabilityChanged()
```

#### Discussion

In response, the system refreshes the text interaction gestures, depending on the value of `isEditable`

## See Also

- [func refreshKeyboardUI()](betextinteraction/refreshkeyboardui.md)
  Tells the system to refresh the keyboard UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/editabilitychanged())*