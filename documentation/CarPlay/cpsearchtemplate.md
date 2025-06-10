# CPSearchTemplate

**Framework**: CarPlay  
**Kind**: class

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

#### Overview

Use this template to provide the ability to search for a destination. When CarPlay displays the template, the user sees a search field, a Cancel button, and a localized keyboard. The template also shows the list of search results after your app completes the search request.

> **Note**:  Some vehicles may limit the display of the keyboard. Check the [`limitedUserInterfaces`](cpsessionconfiguration/limiteduserinterfaces.md) property to determine whether there are limits.

To use a search template, create an instance of [`CPSearchTemplate`](cpsearchtemplate.md) and set its [`delegate`](cpsearchtemplate/delegate.md) to an object that conforms to the [`CPSearchTemplateDelegate`](cpsearchtemplatedelegate.md) protocol. Push the template onto the navigation hierarchy by calling [`pushTemplate(_:animated:completion:)`](cpinterfacecontroller/pushtemplate(_:animated:completion:).md) on the interface controller. This presents the search template to the user.

As the user enters text into the search field, the system calls the delegate method [`searchTemplate(_:updatedSearchText:completionHandler:)`](cpsearchtemplatedelegate/searchtemplate(_:updatedsearchtext:completionhandler:).md), indicating that your app should retrieve the search result. After retrieving the results, call `completionHandler` to return an array of [`CPListItem`](cplistitem.md) objects—one list item for each search result item.

When the user selects an item from the search result, the system calls the [`searchTemplate(_:selectedResult:completionHandler:)`](cpsearchtemplatedelegate/searchtemplate(_:selectedresult:completionhandler:).md) method on the delegate object. The delegate performs any necessary operations to process the selected item, then calls the completion handler to let the system know it can continue.

## Topics

### Providing a Search Template Delegate
- [var delegate: (any CPSearchTemplateDelegate)?](cpsearchtemplate/delegate.md)
  The object that serves as the search template’s delegate.
- [protocol CPSearchTemplateDelegate](cpsearchtemplatedelegate.md)
  The interface for an object that serves as the search template’s delegate.

## Relationships

### Inherits From
- [CPTemplate](cptemplate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Integrating CarPlay with Your Navigation App](integrating-carplay-with-your-navigation-app.md)
  Configure your navigation app to work with CarPlay by displaying your custom map and directions.
- [class CPTemplateApplicationDashboardScene](cptemplateapplicationdashboardscene.md)
  A CarPlay scene that controls your app’s dashboard navigation window.
- [protocol CPTemplateApplicationDashboardSceneDelegate](cptemplateapplicationdashboardscenedelegate.md)
  The methods for responding to the life-cycle events of your navigation app’s dashboard scene.
- [class CPMapTemplate](cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPVoiceControlTemplate](cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplate)*