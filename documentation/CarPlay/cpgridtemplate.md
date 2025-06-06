# CPGridTemplate

**Framework**: CarPlay  
**Kind**: class

A template that displays and manages a grid of items.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPGridTemplate
```

#### Overview

Use this template to display a grid of items as buttons. When creating the grid template, provide an array of [`CPGridButton`](cpgridbutton.md) objects. Each button contains a title, an image, and an optional handler that the system invokes after the user taps the button on the CarPlay screen.

When there are more than eight buttons in the array, the template displays only the first eight. When there are more than four buttons, the template balances the display of the buttons betweem two rows.

## Topics

### Creating a Grid Template
- [init(title: String?, gridButtons: [CPGridButton])](cpgridtemplate/init(title:gridbuttons:).md)
  Creates a grid template with a title and a set of buttons.
- [class CPGridButton](cpgridbutton.md)
  A menu item button displayed on a grid template.
### Getting the Grid Title
- [var title: String](cpgridtemplate/title.md)
  The title shown in the grid template’s navigation bar.
### Getting the Grid Buttons
- [var gridButtons: [CPGridButton]](cpgridtemplate/gridbuttons.md)
  The array of grid buttons displayed on the template.
### Instance Methods
- [func updateGridButtons([CPGridButton])](cpgridtemplate/updategridbuttons(_:).md)
- [func updateTitle(String)](cpgridtemplate/updatetitle(_:).md)

## Relationships

### Inherits From
- [CPTemplate](cptemplate.md)
### Conforms To
- [CPBarButtonProviding](cpbarbuttonproviding.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CPListTemplate](cplisttemplate.md)
  A template that displays and manages a list of items.
- [class CPTabBarTemplate](cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
- [class CPTemplate](cptemplate.md)
  An abstract base class for interface templates.
- [protocol CPBarButtonProviding](cpbarbuttonproviding.md)
  The methods that templates use to provide buttons for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridtemplate)*