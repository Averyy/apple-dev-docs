# CPBarButton

**Framework**: CarPlay  
**Kind**: class

A button for placement in a navigation bar.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPBarButton
```

## Topics

### Creating a CarPlay Bar Button
- [init?(coder: NSCoder)](cpbarbutton/init(coder:).md)
  Creates a button initialized  from data in the specified coder object.
- [init(type: CPBarButton.Type, handler: CPBarButtonHandler?)](cpbarbutton/init(type:handler:).md)
  Creates a bar button with a type and handler.
- [init(image: UIImage, handler: CPBarButtonHandler?)](cpbarbutton/init(image:handler:).md)
  Creates a bar button that displays an image.
- [init(title: String, handler: CPBarButtonHandler?)](cpbarbutton/init(title:handler:).md)
  Creates a bar button that displays a text label.
- [CPBarButton.Type](cpbarbutton/type.md)
  Types of bar buttons.
- [typealias CPBarButtonHandler](cpbarbuttonhandler.md)
  A block that CarPlay calls when the user taps a bar button.
### Configuring the Button
- [var isEnabled: Bool](cpbarbutton/isenabled.md)
  A Boolean value that enables and disables the bar button.
- [var image: UIImage?](cpbarbutton/image.md)
  The image displayed on the bar button.
- [var title: String?](cpbarbutton/title.md)
  The title displayed on the bar button.
### Getting the Button Style
- [var buttonType: CPBarButton.Type](cpbarbutton/buttontype.md)
  The display type for the bar button.
- [var buttonStyle: CPBarButtonStyle](cpbarbutton/buttonstyle.md)
  The style to use when displaying the button.
- [enum CPBarButtonStyle](cpbarbuttonstyle.md)
  The display style of a bar button.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CPMessageComposeBarButton](cpmessagecomposebarbutton.md)
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

- [var backButton: CPBarButton?](cpbarbuttonproviding/backbutton.md)
  A button to display as the Back button on the navigation bar.
- [var leadingNavigationBarButtons: [CPBarButton]](cpbarbuttonproviding/leadingnavigationbarbuttons.md)
  An array of bar buttons to display on the leading side of the navigation bar.
- [var trailingNavigationBarButtons: [CPBarButton]](cpbarbuttonproviding/trailingnavigationbarbuttons.md)
  An array of bar buttons to display on the trailing side of the navigation bar.
- [class CPMessageComposeBarButton](cpmessagecomposebarbutton.md)
  A button that activates Siri and initiates the compose message flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton)*