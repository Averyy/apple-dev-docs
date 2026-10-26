# UIButtonConfigurationIndicatorAutomatic

**Framework**: UIKit  
**Kind**: case  
**Role**: Enumeration Case

A constant that automatically determines an indicator style according to the button’s properties.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```c
UIButtonConfigurationIndicatorAutomatic
```

#### Discussion

With this behavior, the system automatically shows an indicator if the button shows a menu and has single-selection behavior (when its [`isContextMenuInteractionEnabled`](../uicontrol/iscontextmenuinteractionenabled.md), [`showsMenuAsPrimaryAction`](../uicontrol/showsmenuasprimaryaction.md), and [`changesSelectionAsPrimaryAction`](../uibutton/changesselectionasprimaryaction.md) properties are [`true`](../../Swift/true.md)).

## See Also

### Indicator styles
- [UIButtonConfigurationIndicatorNone](./uibuttonconfigurationindicatornone.md)
  A constant that doesn’t show an indicator.
- [UIButtonConfigurationIndicatorPopup](./uibuttonconfigurationindicatorpopup.md)
  A constant that shows a popup-style indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfigurationindicator/uibuttonconfigurationindicatorautomatic)*