# accessibilityLinkedUIElements

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The elements that have links with the accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (copy, nullable) NSArray * accessibilityLinkedUIElements;
```

#### Discussion

Use this property to define a relationship between different user interface elements. For example, use this property to link a list item with contents displayed in another pane or window.

## See Also

### Configuring linkage elements
- [accessibilityServesAsTitleForUIElements](./accessibilityservesastitleforuielements.md)
  The list of elements that the accessibility element is a title for.
- [accessibilityTitleUIElement](./accessibilitytitleuielement.md)
  A static text element that represents the accessibility element’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilitylinkeduielements)*