# CPButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button that displays an image and invokes a handler when the user taps it.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPButton
```

```objc
@interface CPButton : NSObject
```

## Overview

You create instances of `CPButton` to provide a template’s actions. The button displays a custom image that communicates its function. When a user taps the button, CarPlay invokes the handler you provide. The template that contains the button manages its appearance.

The framework provides specialized subclasses for common actions, such as [`CPContactCallButton`](./cpcontactcallbutton.md) or [`CPContactMessageButton`](./cpcontactmessagebutton.md).

## Topics

### Creating a button
- [init(image: UIImage, handler: ((CPButton) -> Void)?)](./cpbutton/init%28image,handler%29.md)
  Creates a button that displays an image and invokes a handler when the user taps it.
- [let CPButtonMaximumImageSize: CGSize](./cpbuttonmaximumimagesize.md)
  The maximum size of a button’s image that CarPlay supports.
### Getting the button’s content
- [var image: UIImage?](./cpbutton/image.md)
  The button’s image.
- [var title: String?](./cpbutton/title.md)
  The button’s title.
### Enabling and disabling the button
- [var isEnabled: Bool](./cpbutton/isenabled.md)
  A Boolean value that determines whether the button is in an enabled state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CPContactCallButton](./cpcontactcallbutton.md)
- [CPContactDirectionsButton](./cpcontactdirectionsbutton.md)
- [CPContactMessageButton](./cpcontactmessagebutton.md)
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
- [class CPTextButton](./cptextbutton.md)
  A button that displays a stylized title.
- [class CPImageSet](./cpimageset.md)
  Light and dark representations of an image.
- [class CPPanel](./cppanel.md)
  A type that provides the common behaviors for panels you display on top of your app’s content.
- [class CPPanelItem](./cppanelitem.md)
  A type that provides the common behaviors for items you display in a section of a panel.
- [class CPPanelButtonConfiguration](./cppanelbuttonconfiguration.md)
  A type that provides the common behaviors for a button layout in a panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbutton)*