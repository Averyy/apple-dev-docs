# PopUpButtonPickerStyle

**Framework**: SwiftUI  
**Kind**: struct

A picker style that presents the options as a menu when the user presses a button.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct PopUpButtonPickerStyle
```

#### Overview

Use this style when there are more than five options. Consider using [`RadioGroupPickerStyle`](radiogrouppickerstyle.md) when there are fewer than five options.

The button itself indicates the selected option. You can include additional controls in the set of options, such as a button to customize the list of options.

To apply this style to a picker, or to a view that contains pickers, use the [`pickerStyle(_:)`](view/pickerstyle(_:).md) modifier.

##### Creating the Picker Style

- [`init()`](popupbuttonpickerstyle/init().md)

## Topics

### Initializers
- [init()](popupbuttonpickerstyle/init.md)
  Creates a pop-up button picker style.

## Relationships

### Conforms To
- [PickerStyle](pickerstyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/popupbuttonpickerstyle)*