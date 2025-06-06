# accessibilityLabel()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns a short description of the slider.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityLabel() -> String?
```

#### Return Value

The description of the slider.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityLabel`](nsaccessibility-c.protocol/accessibilitylabel.md) property.

Do not include the control’s type in the label (for example, use `Volume`, not `Volume slider`). If possible use a single word. To help ensure that accessibility clients such as VoiceOver read the label with the correct intonation, start this label with a capital letter. Do not put a period at the end. Always localize the label.

## See Also

- [func accessibilityPerformDecrement() -> Bool](nsaccessibilityslider/accessibilityperformdecrement.md)
  Decrements the slider’s value.
- [func accessibilityPerformIncrement() -> Bool](nsaccessibilityslider/accessibilityperformincrement.md)
  Increments the slider’s value.
- [func accessibilityValue() -> Any?](nsaccessibilityslider/accessibilityvalue.md)
  Returns the slider’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityslider/accessibilitylabel())*