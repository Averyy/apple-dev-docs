# editabilityChanged()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Tells the system that the document’s editability status has changed.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func editabilityChanged()
```

```objc
- (void) editabilityChanged;
```

## Discussion

In response, the system refreshes the text interaction gestures, depending on the value of `isEditable`

## See Also

### UI updates
- [func refreshKeyboardUI()](./refreshkeyboardui%28%29.md)
  Tells the system to refresh the keyboard UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/editabilitychanged())*