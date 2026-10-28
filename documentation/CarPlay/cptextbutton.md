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

### Creating a Text Button
- [init(title: String, textStyle: CPTextButtonStyle, handler: ((CPTextButton) -> Void)?)](./cptextbutton/init%28title,textstyle,handler%29.md)
  Creates a button that displays a title in a specific style.
### Managing the Title
- [var title: String](./cptextbutton/title.md)
  The text the button displays.
### Managing the Button Style
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

### Location and Information
- [class CPPointOfInterestTemplate](./cppointofinteresttemplate.md)
  A template that displays a map with selectable points of interest.
- [class CPInformationTemplate](./cpinformationtemplate.md)
  A template that provides information for a point of interest, food order, parking location, or charging location.
- [Integrating CarPlay with your quick-ordering app](./integrating-carplay-with-your-quick-ordering-app.md)
  Configure your food-ordering app to work with CarPlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptextbutton)*