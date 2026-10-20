# selectionWillChange(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the system when the selection is about to change in the document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func selectionWillChange(for textInput: any BETextInput)
```

```objc
- (void) selectionWillChangeForTextInput:(id<BETextInput>) textInput;
```

## See Also

### Text selection
- [func selectionDidChange(for: any BETextInput)](./selectiondidchange%28for%29.md)
  Tells the system when the selection has changed in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinputdelegate/selectionwillchange(for:))*