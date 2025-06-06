# NSSharingServicePicker

**Framework**: AppKit  
**Kind**: class

A list of sharing services that the user can choose from.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class NSSharingServicePicker
```

#### Overview

An [`NSSharingServicePicker`](nssharingservicepicker.md) object presents an interface for sharing one or more items using a specific service. In macOS 12 and earlier, this picker displays a menu with a list of services that someone can use to share the item. In macOS 13 and later, the picker displays a popover with a preview of the item and the list of services. When someone chooses a service, the picker automatically shares the proposed item with that service.

Create a sharing service picker and configure it with a delegate object to monitor interactions. Your delegate must conform to the [`NSSharingServicePickerDelegate`](nssharingservicepickerdelegate.md) protocol. Present the picker from your interface using the [`show(relativeTo:of:preferredEdge:)`](nssharingservicepicker/show(relativeto:of:preferrededge:).md) method.

## Topics

### Creating a sharing service picker
- [init(items: [Any])](nssharingservicepicker/init(items:).md)
  Creates a new sharing service picker for the selected items.
### Managing the sharing service picker
- [var delegate: (any NSSharingServicePickerDelegate)?](nssharingservicepicker/delegate.md)
  The object for managing the sharing service picker.
- [protocol NSSharingServicePickerDelegate](nssharingservicepickerdelegate.md)
  An interface for managing content for the macOS share sheet.
### Displaying the sharing service picker
- [func show(relativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge)](nssharingservicepicker/show(relativeto:of:preferrededge:).md)
  Shows the picker interface and populates it with the relevant sharing services.
- [func close()](nssharingservicepicker/close.md)
  Closes the picker interface.
### Retrieving the sharing menu item
- [var standardShareMenuItem: NSMenuItem](nssharingservicepicker/standardsharemenuitem.md)
  A menu item suitable to display the picker for the specified items.
### Classes
- [NSSharingServicePicker.CollaborationModeRestriction](nssharingservicepicker/collaborationmoderestriction.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSSharingService](nssharingservice.md)
  An object that facilitates the sharing of content with social media services, or with apps like Mail or Safari.
- [protocol NSPreviewRepresentableActivityItem](nspreviewrepresentableactivityitem.md)
  An interface you adopt in custom objects that you want to share using the macOS share sheet.
- [class NSSharingServicePickerToolbarItem](nssharingservicepickertoolbaritem.md)
  A toolbar item that displays the macOS share sheet.
- [protocol NSServicesMenuRequestor](nsservicesmenurequestor.md)
  A set of methods that support interaction with items users can share through a sharing service.
- [protocol NSCloudSharingServiceDelegate](nscloudsharingservicedelegate.md)
  A set of methods for responding to the life cycle events of the cloud-sharing service.
- [Services Functions](services-functions.md)
  Configure the contents of your app’s Services menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepicker)*