# accessibilityElement

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (getter=isAccessibilityElement) BOOL accessibilityElement;
```

#### Discussion

Use this property to expose this object to accessibility clients as a functional interface element. For example, when you place a button in a window, the system typically creates a button cell inside a button control inside a container view inside a window. Users, however, don’t care about the view hierarchy details. They should only be told that there’s a button in a window.

If this property is set to [`false`](../../Swift/false.md), accessibility clients ignore this element. By default, `NSView` and its subclasses set this value to [`false`](../../Swift/false.md); however, if your `NSView` subclass adopts one of the accessibility protocols, the system changes the default value to [`true`](../../Swift/true.md).

## See Also

### Related Documentation
- [static func unignoredDescendant(of: Any) -> Any?](../nsaccessibility-swift.struct/unignoreddescendant%28of%29.md)
  Returns an unignored accessibility object, descending the hierarchy, if necessary.
- [static func unignoredAncestor(of: Any) -> Any?](../nsaccessibility-swift.struct/unignoredancestor%28of%29.md)
  Returns an unignored accessibility object, ascending the hierarchy, if necessary.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](../nsaccessibility-swift.struct/unignoredchildrenforonlychild%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredChildren(from: [Any]) -> [Any]](../nsaccessibility-swift.struct/unignoredchildren%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
### Configuring accessibility
- [func isAccessibilitySelectorAllowed(Selector) -> Bool](../nsaccessibilityprotocol/isaccessibilityselectorallowed%28_%29.md)
  Returns a Boolean value that indicates whether assistive apps can invoke the specified selector on the accessibility element.
- [accessibilityEnabled](./accessibilityenabled.md)
  A Boolean value that determines whether the accessibility element responds to user events.
- [accessibilityFrame](./accessibilityframe.md)
  The accessibility element’s frame in screen coordinates.
- [accessibilityHelp](./accessibilityhelp.md)
  The help text for the accessibility element.
- [accessibilityLabel](./accessibilitylabel.md)
  A short description of the accessibility element.
- [accessibilityTitle](./accessibilitytitle.md)
  The title of the accessibility element—for example, a button’s visible text.
- [accessibilityValue](./accessibilityvalue.md)
  The accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityelement)*