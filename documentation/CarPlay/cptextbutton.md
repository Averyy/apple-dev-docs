# CPTextButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button that displays a stylized title.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPTextButton
```

```objc
@interface CPTextButton : NSObject
```

## Overview

You use a text button to attach custom actions to an instance of [`CPPointOfInterest`](./cppointofinterest.md) or [`CPInformationTemplate`](./cpinformationtemplate.md). When creating a button, you provide a closure that CarPlay invokes when the user taps the button. You communicate the button’s purpose using a title and a text style that the button applies to the title.

## Topics

### Creating a text button
- [init(title: String, textStyle: CPTextButtonStyle, handler: ((CPTextButton) -> Void)?)](./cptextbutton/init%28title,textstyle,handler%29.md)
  Creates a button that displays a title in a specific style.
### Managing the title
- [var title: String](./cptextbutton/title.md)
  The text the button displays.
### Managing the button style
- [var textStyle: CPTextButtonStyle](./cptextbutton/textstyle.md)
  The text style the button applies to its title.
- [enum CPTextButtonStyle](./cptextbuttonstyle.md)
  The styles a button can apply to its title to communicate its action.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Common types
- [class CPTemplate](./cptemplate.md)
  An abstract base class for interface templates.
- [class CPButton](./cpbutton.md)
  A button that displays an image and invokes a handler when the user taps it.
- [class CPImageSet](./cpimageset.md)
  Light and dark representations of an image.
- [class CPPanel](./cppanel.md)
  A type that provides the common behaviors for panels you display on top of your app’s content.
- [class CPPanelItem](./cppanelitem.md)
  A type that provides the common behaviors for items you display in a section of a panel.
- [class CPPanelButtonConfiguration](./cppanelbuttonconfiguration.md)
  A type that provides the common behaviors for a button layout in a panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptextbutton)*