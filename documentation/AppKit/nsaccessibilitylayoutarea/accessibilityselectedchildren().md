# accessibilitySelectedChildren()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the layout area’s currently selected children.

**Availability**:
- macOS

## Declaration

```swift
func accessibilitySelectedChildren() -> [Any]?
```

```objc
- (NSArray *) accessibilitySelectedChildren;
```

## Return Value

An array containing the currently selected children. If no children are selected, this method returns an empty array.

## Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilitySelectedChildren`](../nsaccessibility-c.protocol/accessibilityselectedchildren.md) property.

## See Also

### Supporting Accessibility
- [func accessibilityChildren() -> [Any]?](./accessibilitychildren%28%29.md)
  Returns the accessibility element’s children in the accessibility hierarchy.
- [var accessibilityFocusedUIElement: Any](./accessibilityfocuseduielement.md)
  The child accessibility element with the current focus.
- [func accessibilityLabel() -> String](./accessibilitylabel%28%29.md)
  Returns a short description of the layout area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea/accessibilityselectedchildren())*