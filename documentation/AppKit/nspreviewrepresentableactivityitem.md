# NSPreviewRepresentableActivityItem

**Framework**: AppKit  
**Kind**: protocol

An interface you adopt in custom objects that you want to share using the macOS share sheet.

**Availability**:
- macOS 13.0+

## Declaration

```swift
protocol NSPreviewRepresentableActivityItem : NSObjectProtocol
```

#### Overview

Adopt the [`NSPreviewRepresentableActivityItem`](nspreviewrepresentableactivityitem.md) interface in custom types your app makes available for sharing. Use this protocol to specify the item itself and a title and image the share sheet can use to create a preview for your item. To share the item from your app, initialize the [`NSSharingServicePicker`](nssharingservicepicker.md) object with the object that adopts this protocol.

> **Note**:  If your data consists of standard types like strings or images, use an [`NSPreviewRepresentingActivityItem`](nspreviewrepresentingactivityitem.md) object to specify metadata for those types. If your data consists of URLs, pass them directly to the sharing service picker instead of creating a custom preview item.

## Topics

### Providing the Item to Share
- [var item: Any](nspreviewrepresentableactivityitem/item.md)
  The app-specific item you want to share.
### Providing Metadata About the Item
- [var title: String?](nspreviewrepresentableactivityitem/title.md)
  A localized string that contains the name of the item.
- [var imageProvider: NSItemProvider?](nspreviewrepresentableactivityitem/imageprovider.md)
  An object that provides a visual representation of the item.
- [var iconProvider: NSItemProvider?](nspreviewrepresentableactivityitem/iconprovider.md)
  An object that provides an icon that represents the item’s source.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSPreviewRepresentingActivityItem](nspreviewrepresentingactivityitem.md)

## See Also

- [class NSSharingService](nssharingservice.md)
  An object that facilitates the sharing of content with social media services, or with apps like Mail or Safari.
- [class NSSharingServicePicker](nssharingservicepicker.md)
  A list of sharing services that the user can choose from.
- [class NSSharingServicePickerToolbarItem](nssharingservicepickertoolbaritem.md)
  A toolbar item that displays the macOS share sheet.
- [protocol NSServicesMenuRequestor](nsservicesmenurequestor.md)
  A set of methods that support interaction with items users can share through a sharing service.
- [protocol NSCloudSharingServiceDelegate](nscloudsharingservicedelegate.md)
  A set of methods for responding to the life cycle events of the cloud-sharing service.
- [Services Functions](services-functions.md)
  Configure the contents of your app’s Services menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspreviewrepresentableactivityitem)*