# key

**Framework**: AppKit  
**Kind**: property

The unique name of this image component instance.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var key: NSDraggingItem.ImageComponentKey { get set }
```

#### Discussion

The key must be unique for each component in an [`NSDraggingItem`](nsdraggingitem.md) instance. You can create your own named components, however the keys described in [`NSDragImage Component Keys`](nsdragimage-component-keys.md) have special meanings.

When an NSDraggingItem instances [`imageComponents`](nsdraggingitem/imagecomponents.md) are changed by one of the `enumerateDraggingItemsWithOptions:forView:classes:searchOptions:usingBlock:` methods the image associated with this key is morphed into the new image component’s image associated with the same key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/key)*