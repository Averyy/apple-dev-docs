# NSSharingServicePickerToolbarItem

**Framework**: AppKit  
**Kind**: class

A toolbar item that displays the macOS share sheet.

**Availability**:
- iOS 10.13+
- iPadOS 10.13+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSSharingServicePickerToolbarItem
```

#### Overview

An [`NSSharingServicePickerToolbarItem`](nssharingservicepickertoolbaritem.md) object is a standard item you add to your window’s toolbar. When someone clicks it, the item displays the macOS share sheet. Use this item to share the selected or focal content from the current window. For example, you might share the photo someone is viewing, the currently selected text, or the window’s associated document.

Provide the items to share using the associated [`delegate`](nssharingservicepickertoolbaritem/delegate.md) object. For an app built using Mac Catalyst, provide the items from the object in the [`activityItemsConfiguration`](nssharingservicepickertoolbaritem/activityitemsconfiguration.md) property.

## Topics

### Getting the Toolbar Items
- [var delegate: (any NSSharingServicePickerToolbarItemDelegate)?](nssharingservicepickertoolbaritem/delegate.md)
  The custom object from your app that provides the items to share.
- [protocol NSSharingServicePickerToolbarItemDelegate](nssharingservicepickertoolbaritemdelegate.md)
  An interface that provides the content to share from the macOS share sheet.
- [var activityItemsConfiguration: (any UIActivityItemsConfigurationReading)?](nssharingservicepickertoolbaritem/activityitemsconfiguration.md)
  The custom object from an app built with Mac Catalyst that provides the items to share.

## Relationships

### Inherits From
- [NSToolbarItem](nstoolbaritem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSSharingService](nssharingservice.md)
  An object that facilitates the sharing of content with social media services, or with apps like Mail or Safari.
- [class NSSharingServicePicker](nssharingservicepicker.md)
  A list of sharing services that the user can choose from.
- [protocol NSPreviewRepresentableActivityItem](nspreviewrepresentableactivityitem.md)
  An interface you adopt in custom objects that you want to share using the macOS share sheet.
- [protocol NSServicesMenuRequestor](nsservicesmenurequestor.md)
  A set of methods that support interaction with items users can share through a sharing service.
- [protocol NSCloudSharingServiceDelegate](nscloudsharingservicedelegate.md)
  A set of methods for responding to the life cycle events of the cloud-sharing service.
- [Services Functions](services-functions.md)
  Configure the contents of your app’s Services menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertoolbaritem)*