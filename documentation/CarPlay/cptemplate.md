# CPTemplate

**Framework**: CarPlay  
**Kind**: class

An abstract base class for interface templates.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPTemplate
```

#### Overview

`CPTemplate` is an abstract base class for defining CarPlay user interface templates. It provides the common functionality present in all templates.

You don’t use this class directly, or create your own subclasses. Instead, you must use one of the prebuilt templates, such as [`CPListTemplate`](cplisttemplate.md) or [`CPGridTemplate`](cpgridtemplate.md).

## Topics

### Accessing Template Information
- [var userInfo: Any?](cptemplate/userinfo.md)
  Any custom data or object that you want to associate with the template.
### Accessing Tab Information
- [var tabTitle: String?](cptemplate/tabtitle.md)
  A short title that describes the content of the tab.
- [var tabImage: UIImage?](cptemplate/tabimage.md)
  An image that represents the content of the tab.
- [var tabSystemItem: UITabBarItem.SystemItem](cptemplate/tabsystemitem.md)
  A system object that provides a title and image for common tab content, such as contacts or favorites.
- [var showsTabBadge: Bool](cptemplate/showstabbadge.md)
  An indicator you use to call attention to the tab.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CPActionSheetTemplate](cpactionsheettemplate.md)
- [CPAlertTemplate](cpalerttemplate.md)
- [CPContactTemplate](cpcontacttemplate.md)
- [CPGridTemplate](cpgridtemplate.md)
- [CPInformationTemplate](cpinformationtemplate.md)
- [CPListTemplate](cplisttemplate.md)
- [CPMapTemplate](cpmaptemplate.md)
- [CPNowPlayingTemplate](cpnowplayingtemplate.md)
- [CPPointOfInterestTemplate](cppointofinteresttemplate.md)
- [CPSearchTemplate](cpsearchtemplate.md)
- [CPTabBarTemplate](cptabbartemplate.md)
- [CPVoiceControlTemplate](cpvoicecontroltemplate.md)
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

- [class CPListTemplate](cplisttemplate.md)
  A template that displays and manages a list of items.
- [class CPGridTemplate](cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPTabBarTemplate](cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
- [protocol CPBarButtonProviding](cpbarbuttonproviding.md)
  The methods that templates use to provide buttons for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplate)*