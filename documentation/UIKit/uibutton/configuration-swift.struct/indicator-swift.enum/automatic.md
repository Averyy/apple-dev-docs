# UIButton.Configuration.Indicator.automatic

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A constant that automatically determines an indicator style according to the button’s properties.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS

## Declaration

```swift
case automatic
```

## Discussion

With this behavior, the system automatically shows an indicator if the button shows a menu and has single-selection behavior (when its [`isContextMenuInteractionEnabled`](../../../uicontrol/iscontextmenuinteractionenabled.md), [`showsMenuAsPrimaryAction`](../../../uicontrol/showsmenuasprimaryaction.md), and [`changesSelectionAsPrimaryAction`](../../changesselectionasprimaryaction.md) properties are [`true`](../../../../Swift/true.md)).

## See Also

### Indicator styles
- [UIButton.Configuration.Indicator.none](./none.md)
  A constant that doesn’t show an indicator.
- [UIButton.Configuration.Indicator.popup](./popup.md)
  A constant that shows a popup-style indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/indicator-swift.enum/automatic)*