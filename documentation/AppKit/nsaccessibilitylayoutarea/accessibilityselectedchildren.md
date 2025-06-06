# accessibilitySelectedChildren()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the layout area’s currently selected children.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilitySelectedChildren() -> [Any]?
```

#### Return Value

An array containing the currently selected children. If no children are selected, this method returns an empty array.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilitySelectedChildren`](nsaccessibility-c.protocol/accessibilityselectedchildren.md) property.

## See Also

- [func accessibilityChildren() -> [Any]?](nsaccessibilitylayoutarea/accessibilitychildren.md)
  Returns the accessibility element’s children in the accessibility hierarchy.
- [var accessibilityFocusedUIElement: Any](nsaccessibilitylayoutarea/accessibilityfocuseduielement.md)
  The child accessibility element with the current focus.
- [func accessibilityLabel() -> String](nsaccessibilitylayoutarea/accessibilitylabel.md)
  Returns a short description of the layout area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea/accessibilityselectedchildren())*