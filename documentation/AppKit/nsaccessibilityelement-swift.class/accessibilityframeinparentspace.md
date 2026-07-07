# accessibilityFrameInParentSpace

**Framework**: AppKit  
**Kind**: property

The accessibility element’s frame in its parent’s coordinate system.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@property NSRect accessibilityFrameInParentSpace;
```

#### Discussion

Setting this property ensures that the accessibility client receives the correct frame (in screen coordinates) as the element’s parent moves.

## See Also

- [class func element(withRole: NSAccessibility.Role, frame: NSRect, label: String?, parent: Any?) -> Any](nsaccessibilityelement-swift.class/element(withrole:frame:label:parent:).md)
  Instantiates and configures a new accessibility element.
- [func accessibilityAddChildElement(NSAccessibilityElement)](nsaccessibilityelement-swift.class/accessibilityaddchildelement(_:).md)
  Adds a child to the accessibility element in the accessibility hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelement-swift.class/accessibilityframeinparentspace)*