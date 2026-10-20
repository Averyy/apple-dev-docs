# accessibilityChildrenInNavigationOrder()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the array of child accessibility elements in order for linear navigation.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func accessibilityChildrenInNavigationOrder() -> [any NSAccessibilityElementProtocol]?
```

## See Also

### Determining relationships
- [func accessibilityChildren() -> [Any]?](./accessibilitychildren%28%29.md)
  Returns the child accessibility elements in the accessibility hierarchy.
- [func setAccessibilityChildren([Any]?)](./setaccessibilitychildren%28_%29.md)
  Sets the child accessibility elements in the accessibility hierarchy.
- [func setAccessibilityChildrenInNavigationOrder([any NSAccessibilityElementProtocol]?)](./setaccessibilitychildreninnavigationorder%28_%29.md)
  Sets the array of child accessibility elements in order for linear navigation.
- [func accessibilityParent() -> Any?](./accessibilityparent%28%29.md)
  Returns the accessibility element’s parent in the accessibility hierarchy.
- [func setAccessibilityParent(Any?)](./setaccessibilityparent%28_%29.md)
  Sets the accessibility element’s parent in the accessibility hierarchy.
- [func accessibilitySelectedChildren() -> [Any]?](./accessibilityselectedchildren%28%29.md)
  Returns the accessibility element’s currently selected children.
- [func setAccessibilitySelectedChildren([Any]?)](./setaccessibilityselectedchildren%28_%29.md)
  Sets the accessibility element’s currently selected children.
- [func accessibilityTopLevelUIElement() -> Any?](./accessibilitytopleveluielement%28%29.md)
  Returns the top-level element that contains the accessibility element.
- [func setAccessibilityTopLevelUIElement(Any?)](./setaccessibilitytopleveluielement%28_%29.md)
  Sets the top-level element that contains the accessibility element.
- [func accessibilityVisibleChildren() -> [Any]?](./accessibilityvisiblechildren%28%29.md)
  Returns the accessibility element’s visible child accessibility elements.
- [func setAccessibilityVisibleChildren([Any]?)](./setaccessibilityvisiblechildren%28_%29.md)
  Sets the accessibility element’s visible child accessibility elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilitychildreninnavigationorder())*