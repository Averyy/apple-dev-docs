# setAccessibilityFrameInParentSpace(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the accessibility element’s frame in its parent’s coordinate system.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setAccessibilityFrameInParentSpace(_ accessibilityFrameInParentSpace: NSRect)
```

## See Also

### Supporting the Accessibility Hierarchy
- [class func element(withRole: NSAccessibility.Role, frame: NSRect, label: String?, parent: Any?) -> Any](./element%28withrole,frame,label,parent%29.md)
  Instantiates and configures a new accessibility element.
- [func accessibilityAddChildElement(NSAccessibilityElement)](./accessibilityaddchildelement%28_%29.md)
  Adds a child to the accessibility element in the accessibility hierarchy.
- [func accessibilityFrameInParentSpace() -> NSRect](./accessibilityframeinparentspace%28%29.md)
  Returns the accessibility element’s frame in its parent’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelement-swift.class/setaccessibilityframeinparentspace(_:))*