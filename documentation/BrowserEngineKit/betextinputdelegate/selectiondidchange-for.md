# selectionDidChange(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Tells the system when the selection has changed in the document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func selectionDidChange(for textInput: any BETextInput)
```

#### Discussion

This method results in an document state refresh with an invocation to: -[BETextInput requestTextContextForAutocorrectionWithCompletionHandler:]

## See Also

- [func selectionWillChange(for: any BETextInput)](betextinputdelegate/selectionwillchange(for:).md)
  Tells the system when the selection is about to change in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinputdelegate/selectiondidchange(for:))*