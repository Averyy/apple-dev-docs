# CPBarButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button that appears in a navigation bar.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPBarButton
```

```objc
@interface CPBarButton : NSObject
```

## Overview

A `CPBarButton` object is a button you display in the navigation bar of one of your app’s templates. Create buttons when you want to make custom actions available at all times from the template. For example, you might add a plus button to a list template to support adding items to the list. Configure buttons with either an image or custom text you provide.

> **Note**: The back button always displays the system standard appearance, even if you provide a button with a custom image or text.

## Topics

### Creating a bar button
- [init(image: UIImage, handler: CPBarButtonHandler?)](./cpbarbutton/init%28image,handler%29.md)
  Creates a bar button that displays an image.
- [init(title: String, handler: CPBarButtonHandler?)](./cpbarbutton/init%28title,handler%29.md)
  Creates a bar button that displays a text string.
- [typealias CPBarButtonHandler](./cpbarbuttonhandler.md)
  A block that CarPlay calls when the user taps a bar button.
- [init?(coder: NSCoder)](./cpbarbutton/init%28coder%29.md)
### Configuring the button
- [var image: UIImage?](./cpbarbutton/image.md)
  The image to display in the button.
- [var title: String?](./cpbarbutton/title.md)
  The text to display in the button.
- [var isEnabled: Bool](./cpbarbutton/isenabled.md)
  A Boolean value that indicates whether the button is enabled.
### Getting the display style
- [var buttonStyle: CPBarButtonStyle](./cpbarbutton/buttonstyle.md)
  The style to apply to the button.
- [enum CPBarButtonStyle](./cpbarbuttonstyle.md)
  The display style of a bar button.
### Deprecated
- [init(type: CPBarButton.Type, handler: CPBarButtonHandler?)](./cpbarbutton/init%28type,handler%29.md)
- [var buttonType: CPBarButton.Type](./cpbarbutton/buttontype.md)
- [CPBarButton.Type](./cpbarbutton/type.md)
  Specifies the type of a @c CPBarButton.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CPMessageComposeBarButton](./cpmessagecomposebarbutton.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Navigation bar
- [protocol CPBarButtonProviding](./cpbarbuttonproviding.md)
  The interface templates you use to manage buttons in the navigation bar.
- [class CPMessageComposeBarButton](./cpmessagecomposebarbutton.md)
  A button that activates Siri and initiates the process for composing a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton)*