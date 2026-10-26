# accessibilityTitleUIElement

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A static text element that represents the accessibility element’s title.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (weak, nullable) id accessibilityTitleUIElement;
```

#### Discussion

Use this property to associate a static text label with another element—for example, to associate a label with its corresponding text field.

## See Also

### Configuring linkage elements
- [accessibilityLinkedUIElements](./accessibilitylinkeduielements.md)
  The elements that have links with the accessibility element.
- [accessibilityServesAsTitleForUIElements](./accessibilityservesastitleforuielements.md)
  The list of elements that the accessibility element is a title for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilitytitleuielement)*