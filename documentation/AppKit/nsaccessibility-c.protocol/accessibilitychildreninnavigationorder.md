# accessibilityChildrenInNavigationOrder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of child accessibility elements in order for linear navigation.

**Availability**:
- macOS 10.13+

## Declaration

```objc
@property (copy, nullable) NSArray<id<NSAccessibilityElement>> * accessibilityChildrenInNavigationOrder;
```

#### Discussion

The array should match all elements found in [`accessibilityChildren`](./accessibilitychildren.md), rearranged in an easily navigable order.

## See Also

### Determining relationships
- [accessibilityChildren](./accessibilitychildren.md)
  The child accessibility elements in the accessibility hierarchy.
- [accessibilityParent](./accessibilityparent.md)
  The accessibility element’s parent in the accessibility hierarchy.
- [accessibilitySelectedChildren](./accessibilityselectedchildren.md)
  The accessibility element’s currently selected children.
- [accessibilityTopLevelUIElement](./accessibilitytopleveluielement.md)
  The top-level element that contains the accessibility element.
- [accessibilityVisibleChildren](./accessibilityvisiblechildren.md)
  The accessibility element’s visible child accessibility elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilitychildreninnavigationorder)*