# accessibilityChildren

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The child accessibility elements in the accessibility hierarchy.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (copy, nullable) NSArray * accessibilityChildren;
```

## Discussion

This property contains references to child elements in the accessibility hierarchy. If you create an [`NSView`](../nsview.md) subclass, you don’t typically need to set this value. The system automatically populates the `accessibilityChildren` property with descendants in the view hierarchy that are also in the accessibility hierarchy. If you use an [`NSAccessibilityElement`](../nsaccessibilityelement-swift.class.md) subclass to represent an interface element that is not backed by a view, you can either set the `accessibilityChildren` property or you can call the [`accessibilityAddChildElement(_:)`](../nsaccessibilityelement-swift.class/accessibilityaddchildelement%28_%29.md) convenience method.

## See Also

### Related Documentation
- [func accessibilityAddChildElement(NSAccessibilityElement)](../nsaccessibilityelement-swift.class/accessibilityaddchildelement%28_%29.md)
  Adds a child to the accessibility element in the accessibility hierarchy.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](../nsaccessibility-swift.struct/unignoredchildrenforonlychild%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredChildren(from: [Any]) -> [Any]](../nsaccessibility-swift.struct/unignoredchildren%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [accessibilityElement](./accessibilityelement.md)
  A Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
### Determining relationships
- [accessibilityChildrenInNavigationOrder](./accessibilitychildreninnavigationorder.md)
  An array of child accessibility elements in order for linear navigation.
- [accessibilityParent](./accessibilityparent.md)
  The accessibility element’s parent in the accessibility hierarchy.
- [accessibilitySelectedChildren](./accessibilityselectedchildren.md)
  The accessibility element’s currently selected children.
- [accessibilityTopLevelUIElement](./accessibilitytopleveluielement.md)
  The top-level element that contains the accessibility element.
- [accessibilityVisibleChildren](./accessibilityvisiblechildren.md)
  The accessibility element’s visible child accessibility elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilitychildren)*