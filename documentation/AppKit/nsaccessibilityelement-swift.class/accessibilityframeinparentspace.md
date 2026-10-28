# accessibilityFrameInParentSpace

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The accessibility element’s frame in its parent’s coordinate system.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property NSRect accessibilityFrameInParentSpace;
```

## Discussion

Setting this property ensures that the accessibility client receives the correct frame (in screen coordinates) as the element’s parent moves.

## See Also

### Supporting the Accessibility Hierarchy
- [class func element(withRole: NSAccessibility.Role, frame: NSRect, label: String?, parent: Any?) -> Any](./element%28withrole,frame,label,parent%29.md)
  Instantiates and configures a new accessibility element.
- [func accessibilityAddChildElement(NSAccessibilityElement)](./accessibilityaddchildelement%28_%29.md)
  Adds a child to the accessibility element in the accessibility hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelement-swift.class/accessibilityframeinparentspace)*