# CPSearchTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A template that provides the ability to search for a destination and see a list of search results.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPSearchTemplate
```

```objc
@interface CPSearchTemplate : CPTemplate
```

## Overview

Use this template to provide the ability to search for a destination. When CarPlay displays the template, the user sees a search field, a Cancel button, and a localized keyboard. The template also shows the list of search results after your app completes the search request.

> **Note**:  Some vehicles may limit the display of the keyboard. Check the [`limitedUserInterfaces`](./cpsessionconfiguration/limiteduserinterfaces.md) property to determine whether there are limits.

To use a search template, create an instance of [`CPSearchTemplate`](./cpsearchtemplate.md) and set its [`delegate`](./cpsearchtemplate/delegate.md) to an object that conforms to the [`CPSearchTemplateDelegate`](./cpsearchtemplatedelegate.md) protocol. Push the template onto the navigation hierarchy by calling [`pushTemplate(_:animated:completion:)`](./cpinterfacecontroller/pushtemplate%28_,animated,completion%29.md) on the interface controller. This presents the search template to the user.

As the user enters text into the search field, the system calls the delegate method [`searchTemplate(_:updatedSearchText:completionHandler:)`](./cpsearchtemplatedelegate/searchtemplate%28_,updatedsearchtext,completionhandler%29.md), indicating that your app should retrieve the search result. After retrieving the results, call `completionHandler` to return an array of [`CPListItem`](./cplistitem.md) objects—one list item for each search result item.

When the user selects an item from the search result, the system calls the [`searchTemplate(_:selectedResult:completionHandler:)`](./cpsearchtemplatedelegate/searchtemplate%28_,selectedresult,completionhandler%29.md) method on the delegate object. The delegate performs any necessary operations to process the selected item, then calls the completion handler to let the system know it can continue.

## Topics

### Managing search behaviors
- [var delegate: (any CPSearchTemplateDelegate)?](./cpsearchtemplate/delegate.md)
  The object that serves as the search template’s delegate.
- [protocol CPSearchTemplateDelegate](./cpsearchtemplatedelegate.md)
  The interface for an object that serves as the search template’s delegate.

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
- [class CPVoiceControlTemplate](./cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertTemplate](./cpalerttemplate.md)
  A template that displays a modal alert.
- [All templates and supporting types](./all-templates-and-supporting-types.md)
  Explore the templates you use to build the interface of your CarPlay app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplate)*