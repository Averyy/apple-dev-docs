# CPImageSet

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

Light and dark representations of an image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPImageSet
```

```objc
@interface CPImageSet : NSObject
```

## Overview

CarPlay is set to dark appearance by default in most vehicles, but does provide the option to automatically switch between dark and light appearance. Use an image set to provide images for both appearances, and CarPlay displays the correct one for the current appearance.

## Topics

### Creating an image set
- [init(lightContentImage: UIImage, darkContentImage: UIImage)](./cpimageset/init%28lightcontentimage,darkcontentimage%29.md)
  Creates an image set with light and dark versions of an image.
### Getting the images
- [var lightContentImage: UIImage](./cpimageset/lightcontentimage.md)
  The image the system displays when the user interface style is light.
- [var darkContentImage: UIImage](./cpimageset/darkcontentimage.md)
  The image the system displays when the user interface style is dark.
### Initializers
- [init?(coder: NSCoder)](./cpimageset/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Common types
- [class CPTemplate](./cptemplate.md)
  An abstract base class for interface templates.
- [class CPTextButton](./cptextbutton.md)
  A button that displays a stylized title.
- [class CPButton](./cpbutton.md)
  A button that displays an image and invokes a handler when the user taps it.
- [class CPPanel](./cppanel.md)
  A type that provides the common behaviors for panels you display on top of your app’s content.
- [class CPPanelItem](./cppanelitem.md)
  A type that provides the common behaviors for items you display in a section of a panel.
- [class CPPanelButtonConfiguration](./cppanelbuttonconfiguration.md)
  A type that provides the common behaviors for a button layout in a panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageset)*