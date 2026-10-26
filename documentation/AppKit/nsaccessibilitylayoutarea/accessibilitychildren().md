# accessibilityChildren()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the accessibility element’s children in the accessibility hierarchy.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityChildren() -> [Any]?
```

```objc
- (NSArray *) accessibilityChildren;
```

#### Return Value

An array that contains references to this element’s children in the accessibility hierarchy.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityChildren`](../nsaccessibility-c.protocol/accessibilitychildren.md) property.

## See Also

### Related Documentation
- [func accessibilityAddChildElement(NSAccessibilityElement)](../nsaccessibilityelement-swift.class/accessibilityaddchildelement%28_%29.md)
  Adds a child to the accessibility element in the accessibility hierarchy.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](../nsaccessibility-swift.struct/unignoredchildrenforonlychild%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredChildren(from: [Any]) -> [Any]](../nsaccessibility-swift.struct/unignoredchildren%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [accessibilityVisibleChildren](../nsaccessibility-c.protocol/accessibilityvisiblechildren.md)
  The accessibility element’s visible child accessibility elements.
- [accessibilityElement](../nsaccessibility-c.protocol/accessibilityelement.md)
  A Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [accessibilityChildren](../nsaccessibility-c.protocol/accessibilitychildren.md)
  The child accessibility elements in the accessibility hierarchy.
### Supporting Accessibility
- [var accessibilityFocusedUIElement: Any](./accessibilityfocuseduielement.md)
  The child accessibility element with the current focus.
- [func accessibilityLabel() -> String](./accessibilitylabel%28%29.md)
  Returns a short description of the layout area.
- [func accessibilitySelectedChildren() -> [Any]?](./accessibilityselectedchildren%28%29.md)
  Returns the layout area’s currently selected children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea/accessibilitychildren())*