# iconProvider

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An object that provides an icon that represents the item’s source.

**Availability**:
- macOS 13.0+

## Declaration

```swift
optional var iconProvider: NSItemProvider? { get }
```

```objc
@property (strong, readonly, nullable) NSItemProvider * iconProvider;
```

## Discussion

Typically, the icon is a thumbnail-sized representation of the source app for the content. For example, provide your app’s icon for content you manage.

## See Also

### Providing Metadata About the Item
- [var title: String?](./title.md)
  A localized string that contains the name of the item.
- [var imageProvider: NSItemProvider?](./imageprovider.md)
  An object that provides a visual representation of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspreviewrepresentableactivityitem/iconprovider)*