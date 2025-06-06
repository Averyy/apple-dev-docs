# init(item:title:image:icon:)

**Framework**: AppKit  
**Kind**: init

Creates a metadata object with the title, image, and icon for a shareable item.

**Availability**:
- macOS 13.0+

## Declaration

```swift
convenience init(item: Any, title: String?, image: NSImage?, icon: NSImage?)
```

#### Return Value

An initialized item to share.

## Parameters

- `item`: The item to share from the Mac share sheet. The item must conform to the   protocol, or be an   or   object.
- `title`: The localized name of the item.
- `image`: An image to display as a preview for the item. For example, when you share a URL for a webpage, you might specify the hero image for that page or a rendering of the webpage itself.
- `icon`: A thumbnail-size image of the source of the item. Typically, you specify your app’s icon but you can provide a different icon if the content has a different source.

## See Also

- [init(item: Any, title: String?, imageProvider: NSItemProvider?, iconProvider: NSItemProvider?)](nspreviewrepresentingactivityitem/init(item:title:imageprovider:iconprovider:).md)
  Creates a metadata object that provides a title and images for a shareable item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspreviewrepresentingactivityitem/init(item:title:image:icon:))*