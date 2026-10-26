# accessibilityParent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The accessibility element’s parent in the accessibility hierarchy.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (weak, nullable) id accessibilityParent;
```

#### Discussion

This property must contain a reference to another element in the accessibility hierarchy. If you create an [`NSView`](../nsview.md) subclass, you don’t typically need to set this value. The system automatically sets the parent to the nearest ancestor in the view hierarchy that is also in the accessibility hierarchy. If you use an [`NSAccessibilityElement`](../nsaccessibilityelement-swift.class.md) subclass to represent an interface element that is not backed by a view, you can either set the parent property or you can call the [`element(withRole:frame:label:parent:)`](../nsaccessibilityelement-swift.class/element%28withrole,frame,label,parent%29.md) convenience method, which sets it automatically.

## See Also

### Related Documentation
- [static func unignoredAncestor(of: Any) -> Any?](../nsaccessibility-swift.struct/unignoredancestor%28of%29.md)
  Returns an unignored accessibility object, ascending the hierarchy, if necessary.
- [class func element(withRole: NSAccessibility.Role, frame: NSRect, label: String?, parent: Any?) -> Any](../nsaccessibilityelement-swift.class/element%28withrole,frame,label,parent%29.md)
  Instantiates and configures a new accessibility element.
- [accessibilityElement](./accessibilityelement.md)
  A Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
### Determining relationships
- [accessibilityChildren](./accessibilitychildren.md)
  The child accessibility elements in the accessibility hierarchy.
- [accessibilityChildrenInNavigationOrder](./accessibilitychildreninnavigationorder.md)
  An array of child accessibility elements in order for linear navigation.
- [accessibilitySelectedChildren](./accessibilityselectedchildren.md)
  The accessibility element’s currently selected children.
- [accessibilityTopLevelUIElement](./accessibilitytopleveluielement.md)
  The top-level element that contains the accessibility element.
- [accessibilityVisibleChildren](./accessibilityvisiblechildren.md)
  The accessibility element’s visible child accessibility elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityparent)*