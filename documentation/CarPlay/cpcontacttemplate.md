# CPContactTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A template that displays information about a person or a business.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPContactTemplate
```

```objc
@interface CPContactTemplate : CPTemplate
```

## Overview

The contact template can provide up to four contextual actions a user can invoke. For example, you might have an action that provides directions to the contact’s address.

When creating a contact template, you provide an instance of [`CPContact`](./cpcontact.md) that contains a contact’s name and image, and optional subtitle. The object also contains any actions relevant to the contact. CarPlay provides specialized buttons for common actions, such as [`CPContactCallButton`](./cpcontactcallbutton.md) or [`CPContactMessageButton`](./cpcontactmessagebutton.md).

To display a contact template, call your interface controller’s [`pushTemplate(_:animated:completion:)`](./cpinterfacecontroller/pushtemplate%28_,animated,completion%29.md) method to push it onto the navigation hierarchy, or [`presentTemplate(_:animated:completion:)`](./cpinterfacecontroller/presenttemplate%28_,animated,completion%29.md) to present it modally.

> **Note**:  `CPContactTemplate` is only available in apps that have the communication or navigation entitlements.

## Topics

### Creating a contact template
- [init(contact: CPContact)](./cpcontacttemplate/init%28contact%29.md)
  Creates a contact template that displays the provided contact.
### Configuring the contact
- [var contact: CPContact](./cpcontacttemplate/contact.md)
  The contact that the template displays.
- [class CPContact](./cpcontact.md)
  A data object that contains information about a contact.

## Relationships

### Inherits From
- [CPTemplate](./cptemplate.md)
### Conforms To
- [CPBarButtonProviding](./cpbarbuttonproviding.md)
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
- [class CPSearchTemplate](./cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
- [class CPVoiceControlTemplate](./cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertTemplate](./cpalerttemplate.md)
  A template that displays a modal alert.
- [All templates and supporting types](./all-templates-and-supporting-types.md)
  Explore the templates you use to build the interface of your CarPlay app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontacttemplate)*