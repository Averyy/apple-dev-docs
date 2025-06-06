# nameOfSlideshowItem(at:)

**Framework**: Quartz  
**Kind**: method

Returns the display name for item at the specified index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func nameOfSlideshowItem(at index: Int) -> String!
```

#### Return Value

The display name. For the best user experience, you should provide the localized name, because this string appears in the user interface.

#### Discussion

This method is optional.

## Parameters

- `index`: The index for a slideshow item.

## See Also

- [func numberOfSlideshowItems() -> Int](ikslideshowdatasource/numberofslideshowitems.md)
  Returns the number of items in a slideshow.
- [func slideshowItem(at: Int) -> Any!](ikslideshowdatasource/slideshowitem(at:).md)
  Returns the item for a given index
- [func canExportSlideshowItem(at: Int, toApplication: String!) -> Bool](ikslideshowdatasource/canexportslideshowitem(at:toapplication:).md)
  Reports whether the export button should be enabled for a slideshow item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/nameofslideshowitem(at:))*