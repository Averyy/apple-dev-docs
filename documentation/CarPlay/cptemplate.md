# CPTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

An abstract base class for interface templates.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPTemplate
```

```objc
@interface CPTemplate : NSObject
```

## Overview

`CPTemplate` is an abstract base class for defining CarPlay user interface templates. It provides the common functionality present in all templates.

You don’t use this class directly, or create your own subclasses. Instead, you must use one of the prebuilt templates, such as [`CPListTemplate`](./cplisttemplate.md) or [`CPGridTemplate`](./cpgridtemplate.md).

## Topics

### Accessing tab information
- [var tabTitle: String?](./cptemplate/tabtitle.md)
  A short title that describes the content of the tab.
- [var tabImage: UIImage?](./cptemplate/tabimage.md)
  An image that represents the content of the tab.
- [var tabSystemItem: UITabBarItem.SystemItem](./cptemplate/tabsystemitem.md)
  A system object that provides a title and image for common tab content, such as contacts or favorites.
- [var showsTabBadge: Bool](./cptemplate/showstabbadge.md)
  An indicator you use to call attention to the tab.
### Accessing app-specific details
- [var userInfo: Any?](./cptemplate/userinfo.md)
  Any custom data or object that you want to associate with the template.
### Initializers
- [init?(coder: NSCoder)](./cptemplate/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CPActionSheetTemplate](./cpactionsheettemplate.md)
- [CPAlertTemplate](./cpalerttemplate.md)
- [CPContactTemplate](./cpcontacttemplate.md)
- [CPGridTemplate](./cpgridtemplate.md)
- [CPInformationTemplate](./cpinformationtemplate.md)
- [CPListTemplate](./cplisttemplate.md)
- [CPMapTemplate](./cpmaptemplate.md)
- [CPNowPlayingTemplate](./cpnowplayingtemplate.md)
- [CPPointOfInterestTemplate](./cppointofinteresttemplate.md)
- [CPSearchTemplate](./cpsearchtemplate.md)
- [CPTabBarTemplate](./cptabbartemplate.md)
- [CPVoiceControlTemplate](./cpvoicecontroltemplate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Common types
- [class CPTextButton](./cptextbutton.md)
  A button that displays a stylized title.
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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplate)*