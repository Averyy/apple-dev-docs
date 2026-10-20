# accessibilityAddChildElement(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a child to the accessibility element in the accessibility hierarchy.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityAddChildElement(_ childElement: NSAccessibilityElement)
```

```objc
- (void) accessibilityAddChildElement:(NSAccessibilityElement *) childElement;
```

#### Discussion

Calling this method sets up the proper parent-child relationship between the current element and the provided child element.

## Parameters

- `childElement`: The child element to be added.

## See Also

### Supporting the Accessibility Hierarchy
- [class func element(withRole: NSAccessibility.Role, frame: NSRect, label: String?, parent: Any?) -> Any](./element%28withrole,frame,label,parent%29.md)
  Instantiates and configures a new accessibility element.
- [func accessibilityFrameInParentSpace() -> NSRect](./accessibilityframeinparentspace%28%29.md)
  Returns the accessibility element’s frame in its parent’s coordinate system.
- [func setAccessibilityFrameInParentSpace(NSRect)](./setaccessibilityframeinparentspace%28_%29.md)
  Sets the accessibility element’s frame in its parent’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelement-swift.class/accessibilityaddchildelement(_:))*