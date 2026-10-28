# NSPreviewRepresentingActivityItem

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A type that adds metadata to an item you share using the macOS share sheet.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class NSPreviewRepresentingActivityItem
```

```objc
@interface NSPreviewRepresentingActivityItem : NSObject
```

## Overview

An [`NSPreviewRepresentingActivityItem`](./nspreviewrepresentingactivityitem.md) object provides a concrete implementation of the [`NSPreviewRepresentableActivityItem`](./nspreviewrepresentableactivityitem.md) protocol. Use it to create shareable items for common types such as strings or images, or when you don’t want to adopt the [`NSPreviewRepresentableActivityItem`](./nspreviewrepresentableactivityitem.md) protocol directly in your app’s objects. To share the item from your app, initialize the [`NSSharingServicePicker`](./nssharingservicepicker.md) object with this object.

> **Note**:  If your data consists of a URL, pass that URL directly to the sharing service picker instead of using this class.

## Topics

### Creating a Preview Activity Item
- [convenience init(item: Any, title: String?, image: NSImage?, icon: NSImage?)](./nspreviewrepresentingactivityitem/init%28item,title,image,icon%29.md)
  Creates a metadata object with the title, image, and icon for a shareable item.
- [init(item: Any, title: String?, imageProvider: NSItemProvider?, iconProvider: NSItemProvider?)](./nspreviewrepresentingactivityitem/init%28item,title,imageprovider,iconprovider%29.md)
  Creates a metadata object that provides a title and images for a shareable item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSPreviewRepresentableActivityItem](./nspreviewrepresentableactivityitem.md)

## See Also

### Share Panel
- [class NSSharingServicePicker](./nssharingservicepicker.md)
  A list of sharing services that the user can choose from.
- [protocol NSPreviewRepresentableActivityItem](./nspreviewrepresentableactivityitem.md)
  An interface you adopt in custom objects that you want to share using the macOS share sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspreviewrepresentingactivityitem)*