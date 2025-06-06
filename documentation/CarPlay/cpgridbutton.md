# CPGridButton

**Framework**: CarPlay  
**Kind**: class

A menu item button displayed on a grid template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPGridButton
```

## Topics

### Creating a Grid Button
- [init(titleVariants: [String], image: UIImage, handler: ((CPGridButton) -> Void)?)](cpgridbutton/init(titlevariants:image:handler:).md)
  Creates a grid button with the specified title variants, image, and action handler.
### Controlling the Grid Button
- [var isEnabled: Bool](cpgridbutton/isenabled.md)
  A Boolean value that enables and disables the grid button.
### Obtaining Grid Button Information
- [var titleVariants: [String]](cpgridbutton/titlevariants.md)
  An array of title variants for the button.
- [var image: UIImage](cpgridbutton/image.md)
  The image displayed on the button.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [init(title: String?, gridButtons: [CPGridButton])](cpgridtemplate/init(title:gridbuttons:).md)
  Creates a grid template with a title and a set of buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridbutton)*