# canExportSlideshowItem(at:toApplication:)

**Framework**: Quartz  
**Kind**: method

Reports whether the export button should be enabled for a slideshow item.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func canExportSlideshowItem(at index: Int, toApplication applicationBundleIdentifier: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the export button should be enabled for an item; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func numberOfSlideshowItems() -> Int](ikslideshowdatasource/numberofslideshowitems.md)
  Returns the number of items in a slideshow.
- [func slideshowItem(at: Int) -> Any!](ikslideshowdatasource/slideshowitem(at:).md)
  Returns the item for a given index
- [func nameOfSlideshowItem(at: Int) -> String!](ikslideshowdatasource/nameofslideshowitem(at:).md)
  Returns the display name for item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/canexportslideshowitem(at:toapplication:))*