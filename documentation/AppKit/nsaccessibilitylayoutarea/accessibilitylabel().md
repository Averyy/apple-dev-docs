# accessibilityLabel()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a short description of the layout area.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityLabel() -> String
```

```objc
- (NSString *) accessibilityLabel;
```

## Return Value

The description of the layout area.

## Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityLabel`](../nsaccessibility-c.protocol/accessibilitylabel.md) property.

Do not include the control’s type in the label (for example, use `Canvas`, not `Canvas Layout Area`). If possible use a single word. To help ensure that accessibility clients such as VoiceOver read the label with the correct intonation, start this label with a capital letter. Do not put a period at the end. Always localize the label.

## See Also

### Supporting Accessibility
- [func accessibilityChildren() -> [Any]?](./accessibilitychildren%28%29.md)
  Returns the accessibility element’s children in the accessibility hierarchy.
- [var accessibilityFocusedUIElement: Any](./accessibilityfocuseduielement.md)
  The child accessibility element with the current focus.
- [func accessibilitySelectedChildren() -> [Any]?](./accessibilityselectedchildren%28%29.md)
  Returns the layout area’s currently selected children.
### Related Documentation
- [accessibilityLabel](../nsaccessibility-c.protocol/accessibilitylabel.md)
  A short description of the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea/accessibilitylabel())*