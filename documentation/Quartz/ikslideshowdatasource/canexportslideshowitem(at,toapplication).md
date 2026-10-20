# canExportSlideshowItem(at:toApplication:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Reports whether the export button should be enabled for a slideshow item.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func canExportSlideshowItem(at index: Int, toApplication applicationBundleIdentifier: String!) -> Bool
```

```objc
- (BOOL) canExportSlideshowItemAtIndex:(NSUInteger) index toApplication:(NSString *) applicationBundleIdentifier;
```

#### Return Value

[`true`](../../Swift/true.md) if the export button should be enabled for an item; otherwise [`false`](../../Swift/false.md).

## See Also

### Providing Slideshow Information
- [func numberOfSlideshowItems() -> Int](./numberofslideshowitems%28%29.md)
  Returns the number of items in a slideshow.
- [func slideshowItem(at: Int) -> Any!](./slideshowitem%28at%29.md)
  Returns the item for a given index
- [func nameOfSlideshowItem(at: Int) -> String!](./nameofslideshowitem%28at%29.md)
  Returns the display name for item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/canexportslideshowitem(at:toapplication:))*