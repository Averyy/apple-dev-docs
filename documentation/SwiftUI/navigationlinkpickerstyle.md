# NavigationLinkPickerStyle

**Framework**: SwiftUI  
**Kind**: struct

A picker style represented by a navigation link that presents the options by pushing a List-style picker view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct NavigationLinkPickerStyle
```

#### Overview

In navigation stacks, prefer the default [`menu`](pickerstyle/menu.md) style. Consider the navigation link style when you have a large number of options or your design is better expressed by pushing onto a stack.

You can also use [`navigationLink`](pickerstyle/navigationlink.md) to construct this style.

## Topics

### Creating the picker style
- [init()](navigationlinkpickerstyle/init.md)
  Creates a navigation link picker style.

## Relationships

### Conforms To
- [PickerStyle](pickerstyle.md)

## See Also

- [struct DefaultPickerStyle](defaultpickerstyle.md)
  The default picker style, based on the picker’s context.
- [struct InlinePickerStyle](inlinepickerstyle.md)
  A `PickerStyle` where each option is displayed inline with other views in the current container.
- [struct MenuPickerStyle](menupickerstyle.md)
  A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [struct PalettePickerStyle](palettepickerstyle.md)
  A picker style that presents the options as a row of compact elements.
- [struct RadioGroupPickerStyle](radiogrouppickerstyle.md)
  A picker style that presents the options as a group of radio buttons.
- [struct SegmentedPickerStyle](segmentedpickerstyle.md)
  A picker style that presents the options in a segmented control.
- [struct WheelPickerStyle](wheelpickerstyle.md)
  A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlinkpickerstyle)*