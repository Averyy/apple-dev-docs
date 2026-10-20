# systemWillChangeSelection(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invoked by the system when the selection is about to change in the document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func systemWillChangeSelection(for textInteraction: BETextInteraction)
```

```objc
- (void) systemWillChangeSelectionForInteraction:(BETextInteraction *) textInteraction;
```

## See Also

### Text selection changes
- [func systemDidChangeSelection(for: BETextInteraction)](./systemdidchangeselection%28for%29.md)
  Invoked by the system when the selection is about to change in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteractiondelegate/systemwillchangeselection(for:))*