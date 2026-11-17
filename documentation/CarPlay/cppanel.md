# CPPanel

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that provides the common behaviors for panels you display on top of your app’s content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPPanel
```

```objc
@interface CPPanel : NSObject
```

## Overview

The `CPPanel` type defines the default behaviors for panels you display in your app. You don’t create or present this type directly. Instead, instantiate one of the defined subclasses and present that type from your app’s interface. For example, create a [`CPMapPanel`](./cpmappanel.md) and configure it with navigation-related data, and present it from a [`CPMapTemplate`](./cpmaptemplate.md) to overlay that information on top of your custom map.

## Topics

### Initializing the panel
- [init?(coder: NSCoder)](./cppanel/init%28coder%29.md)
### Adding a close button to the panel
- [var showsCloseButton: Bool](./cppanel/showsclosebutton.md)
  A Boolean value that indicates whether the panel displays a close button.
### Getting the maximum number of items
- [class var maximumPanelItemsCount: Int](./cppanel/maximumpanelitemscount.md)
  The maximum number of items the panel is able to display.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CPMapPanel](./cpmappanel.md)
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
- [class CPImageSet](./cpimageset.md)
  Light and dark representations of an image.
- [class CPPanelItem](./cppanelitem.md)
  A type that provides the common behaviors for items you display in a section of a panel.
- [class CPPanelButtonConfiguration](./cppanelbuttonconfiguration.md)
  A type that provides the common behaviors for a button layout in a panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanel)*