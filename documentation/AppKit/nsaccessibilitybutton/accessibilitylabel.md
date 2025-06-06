# accessibilityLabel()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns a short description of the button.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityLabel() -> String?
```

#### Return Value

The description of this button.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityLabel`](nsaccessibility-c.protocol/accessibilitylabel.md) property.

Do not include the accessibility element’s type in the label (for example, write `Play` not `Play button`.). If possible, use a single word. To help ensure that accessibility clients like VoiceOver read the label with the correct intonation, this label should start with a capital letter. Do not put a period at the end. Always localize the label.

## See Also

- [func accessibilityPerformPress() -> Bool](nsaccessibilitybutton/accessibilityperformpress.md)
  Simulates clicking the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitybutton/accessibilitylabel())*