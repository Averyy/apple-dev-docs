# accessibilityHelp

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The help text for the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (copy, nullable) NSString * accessibilityHelp;
```

#### Discussion

Use this property only when the results of activating this element are not obvious from the element’s label. This string functions as a tooltip. For example, VoiceOver reads this string when you pause over a control. To help ensure that accessibility clients like VoiceOver read the help text with the proper inflection, begin this string with a verb, capitalize the first letter, and end the string with a period. Always localize this string. The default value is `nil`.

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
- [accessibilityLabel](./accessibilitylabel.md)
  A short description of the accessibility element.
- [accessibilityTitle](./accessibilitytitle.md)
  The title of the accessibility element—for example, a button’s visible text.
- [accessibilityValue](./accessibilityvalue.md)
  The accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityhelp)*