# CPAlertTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A template that displays a modal alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPAlertTemplate
```

```objc
@interface CPAlertTemplate : CPTemplate
```

## Overview

You must present alerts modally by calling the [`presentTemplate(_:animated:completion:)`](./cpinterfacecontroller/presenttemplate%28_,animated,completion%29.md) method available on your app’s instance of [`CPInterfaceController`](./cpinterfacecontroller.md). The user dismisses the alert by pressing a button, or you can dismiss it by calling the interface controller’s [`dismissTemplate(animated:completion:)`](./cpinterfacecontroller/dismisstemplate%28animated,completion%29.md) method.

## Topics

### Creating an alert template
- [init(titleVariants: [String], actions: [CPAlertAction])](./cpalerttemplate/init%28titlevariants,actions%29.md)
  Creates an alert template.
- [class var maximumActionCount: Int](./cpalerttemplate/maximumactioncount.md)
  The maximum number of actions allowed in an alert template.
### Getting the alert details
- [var titleVariants: [String]](./cpalerttemplate/titlevariants.md)
  The array of title variants.
- [var actions: [CPAlertAction]](./cpalerttemplate/actions.md)
  The array of actions available on the alert.

## Relationships

### Inherits From
- [CPTemplate](./cptemplate.md)
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
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interface templates
- [class CPTabBarTemplate](./cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
- [class CPListTemplate](./cplisttemplate.md)
  A template that displays a single-column list of items in one of several visual styles.
- [class CPGridTemplate](./cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPMapTemplate](./cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPNowPlayingTemplate](./cpnowplayingtemplate.md)
  A shared system template that shows the currently selected audio content and offers controls to manage playback.
- [class CPPointOfInterestTemplate](./cppointofinteresttemplate.md)
  A template that displays a map with selectable points of interest.
- [class CPInformationTemplate](./cpinformationtemplate.md)
  A template that provides information for a point of interest, food order, parking location, or charging location.
- [class CPContactTemplate](./cpcontacttemplate.md)
  A template that displays information about a person or a business.
- [class CPSearchTemplate](./cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
- [class CPVoiceControlTemplate](./cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [All templates and supporting types](./all-templates-and-supporting-types.md)
  Explore the templates you use to build the interface of your CarPlay app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalerttemplate)*