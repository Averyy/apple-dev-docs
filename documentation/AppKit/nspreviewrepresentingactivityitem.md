# NSPreviewRepresentingActivityItem

**Framework**: Appkit  
**Kind**: class

A type that adds metadata to an item you share using the macOS share sheet.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class NSPreviewRepresentingActivityItem
```

#### Overview

An [`NSPreviewRepresentingActivityItem`](nspreviewrepresentingactivityitem.md) object provides a concrete implementation of the [`NSPreviewRepresentableActivityItem`](nspreviewrepresentableactivityitem.md) protocol. Use it to create shareable items for common types such as strings or images, or when you don’t want to adopt the [`NSPreviewRepresentableActivityItem`](nspreviewrepresentableactivityitem.md) protocol directly in your app’s objects. To share the item from your app, initialize the [`NSSharingServicePicker`](nssharingservicepicker.md) object with this object.

> **Note**:  If your data consists of a URL, pass that URL directly to the sharing service picker instead of using this class.

## Topics

### Creating a Preview Activity Item
- [convenience init(item: Any, title: String?, image: NSImage?, icon: NSImage?)](nspreviewrepresentingactivityitem/init(item:title:image:icon:).md)
  Creates a metadata object with the title, image, and icon for a shareable item.
- [init(item: Any, title: String?, imageProvider: NSItemProvider?, iconProvider: NSItemProvider?)](nspreviewrepresentingactivityitem/init(item:title:imageprovider:iconprovider:).md)
  Creates a metadata object that provides a title and images for a shareable item.

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
- [NSPreviewRepresentableActivityItem](nspreviewrepresentableactivityitem.md)

## See Also

- [class NSSharingServicePicker](nssharingservicepicker.md)
  A list of sharing services that the user can choose from.
- [protocol NSPreviewRepresentableActivityItem](nspreviewrepresentableactivityitem.md)
  An interface you adopt in custom objects that you want to share using the macOS share sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nspreviewrepresentingactivityitem)*