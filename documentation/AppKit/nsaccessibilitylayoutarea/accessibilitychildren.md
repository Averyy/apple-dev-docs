# accessibilityChildren()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the accessibility element’s children in the accessibility hierarchy.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityChildren() -> [Any]?
```

#### Return Value

An array that contains references to this element’s children in the accessibility hierarchy.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityChildren`](nsaccessibility-c.protocol/accessibilitychildren.md) property.

## See Also

- [func accessibilityAddChildElement(NSAccessibilityElement)](nsaccessibilityelement-swift.class/accessibilityaddchildelement(_:).md)
  Adds a child to the accessibility element in the accessibility hierarchy.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](nsaccessibility-swift.struct/unignoredchildrenforonlychild(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredChildren(from: [Any]) -> [Any]](nsaccessibility-swift.struct/unignoredchildren(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [var accessibilityFocusedUIElement: Any](nsaccessibilitylayoutarea/accessibilityfocuseduielement.md)
  The child accessibility element with the current focus.
- [func accessibilityLabel() -> String](nsaccessibilitylayoutarea/accessibilitylabel.md)
  Returns a short description of the layout area.
- [func accessibilitySelectedChildren() -> [Any]?](nsaccessibilitylayoutarea/accessibilityselectedchildren.md)
  Returns the layout area’s currently selected children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea/accessibilitychildren())*