# accessibilityLabel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A short description of the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (copy, nullable) NSString * accessibilityLabel;
```

#### Discussion

Do not include the accessibility element’s type in the label (for example, write `Play`, not `Play button`.). If possible, use a single word. To help ensure that accessibility clients such as VoiceOver read the label with the correct intonation, start this label with a capital letter. Do not put a period at the end. Always localize the label.

## See Also

### Related Documentation
- [accessibilityRoleDescription](./accessibilityroledescription.md)
  A localized, human-intelligible description of the accessibility element’s role, such as *radio button*.
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
- [accessibilityTitle](./accessibilitytitle.md)
  The title of the accessibility element—for example, a button’s visible text.
- [accessibilityValue](./accessibilityvalue.md)
  The accessibility element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilitylabel)*