# accessibilityAddChildElement(_:)

**Framework**: AppKit  
**Kind**: method

Adds a child to the accessibility element in the accessibility hierarchy.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityAddChildElement(_ childElement: NSAccessibilityElement)
```

#### Discussion

Calling this method sets up the proper parent-child relationship between the current element and the provided child element.

## Parameters

- `childElement`: The child element to be added.

## See Also

- [class func element(withRole: NSAccessibility.Role, frame: NSRect, label: String?, parent: Any?) -> Any](nsaccessibilityelement-swift.class/element(withrole:frame:label:parent:).md)
  Instantiates and configures a new accessibility element.
- [func accessibilityFrameInParentSpace() -> NSRect](nsaccessibilityelement-swift.class/accessibilityframeinparentspace.md)
  Returns the accessibility element’s frame in its parent’s coordinate system.
- [func setAccessibilityFrameInParentSpace(NSRect)](nsaccessibilityelement-swift.class/setaccessibilityframeinparentspace(_:).md)
  Sets the accessibility element’s frame in its parent’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelement-swift.class/accessibilityaddchildelement(_:))*