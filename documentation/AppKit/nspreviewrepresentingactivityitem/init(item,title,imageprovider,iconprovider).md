# init(item:title:imageProvider:iconProvider:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a metadata object that provides a title and images for a shareable item.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(item: Any, title: String?, imageProvider: NSItemProvider?, iconProvider: NSItemProvider?)
```

```objc
- (instancetype) initWithItem:(id) item title:(NSString *) title imageProvider:(NSItemProvider *) imageProvider iconProvider:(NSItemProvider *) iconProvider;
```

## Return Value

An initialized item to share.

## Parameters

- `item`: The item to share from the Mac share sheet. The item must conform to the [`NSPasteboardWriting`](../nspasteboardwriting.md) protocol, or be an [`NSItemProvider`](../../Foundation/nsitemprovider.md) or [`NSDocument`](../nsdocument.md) object.
- `title`: The localized name of the item.
- `imageProvider`: An object that provides the image to display as a preview for the item. For example, when you share a URL for a webpage, you might specify the hero image for that page or a rendering of the webpage itself.
- `iconProvider`: An object that a thumbnail-size image of the source of the item. Typically, you specify your app’s icon but you can provide a different icon if the content has a different source.

## See Also

### Creating a Preview Activity Item
- [convenience init(item: Any, title: String?, image: NSImage?, icon: NSImage?)](./init%28item,title,image,icon%29.md)
  Creates a metadata object with the title, image, and icon for a shareable item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspreviewrepresentingactivityitem/init(item:title:imageprovider:iconprovider:))*