# textField(_:didSelect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when an item in the suggestions menu has been selected.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
func textField(_ textField: NSTextField, didSelect item: Self.Item)
```

#### Discussion

The default implementation inserts the item’s text completion (`textField(_:textCompletionFor:)`) into the control, replacing its existing text. Overriding this method allows you to do a custom behavior instead.

## Parameters

- `textField`: The text field whose suggestions item was highlighted.
- `item`: The item that was selected.

## Default Implementations

### NSTextSuggestionsDelegate Implementations
- [func textField(NSTextField, didSelect: Self.Item)](./textfield%28_,didselect%29-1pke6.md)
  Called when an item in the suggestions menu has been selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextsuggestionsdelegate/textfield(_:didselect:))*