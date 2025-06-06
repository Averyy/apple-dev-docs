# imageProvider

**Framework**: AppKit  
**Kind**: property

An object that provides a visual representation of the item.

**Availability**:
- macOS 13.0+

## Declaration

```swift
optional var imageProvider: NSItemProvider? { get }
```

#### Discussion

Provide a full-size representation of the content you’re sharing. For example, if the shared item is a link to a webpage, provide the hero image for that webpage or a rendering of the page.

## See Also

- [var title: String?](nspreviewrepresentableactivityitem/title.md)
  A localized string that contains the name of the item.
- [var iconProvider: NSItemProvider?](nspreviewrepresentableactivityitem/iconprovider.md)
  An object that provides an icon that represents the item’s source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspreviewrepresentableactivityitem/imageprovider)*