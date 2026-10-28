# accessibilityValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The accessibility element’s value.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (strong, nullable) id accessibilityValue;
```

## Discussion

The accessibility protocols for roles that support values typically redefine this property to take a more specific value type. For example, the [`staticText`](../nsaccessibility-swift.struct/role/statictext.md) protocol uses [`NSString`](../../Foundation/nsstring.md) values, and the [`progressIndicator`](../nsaccessibility-swift.struct/role/progressindicator.md) protocol uses [`NSNumber`](../../Foundation/nsnumber.md) values.

## See Also

### Configuring accessibility
- [func isAccessibilitySelectorAllowed(Selector) -> Bool](../nsaccessibilityprotocol/isaccessibilityselectorallowed%28_%29.md)
  Returns a Boolean value that indicates whether assistive apps can invoke the specified selector on the accessibility element.
- [accessibilityElement](./accessibilityelement.md)
  A Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityvalue)*