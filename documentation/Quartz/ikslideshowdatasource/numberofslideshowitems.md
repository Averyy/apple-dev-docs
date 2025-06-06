# numberOfSlideshowItems()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the number of items in a slideshow.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func numberOfSlideshowItems() -> Int
```

#### Return Value

The number of items in the slideshow.

#### Discussion

Your data source must implement this method.

## See Also

- [func slideshowItem(at: Int) -> Any!](ikslideshowdatasource/slideshowitem(at:).md)
  Returns the item for a given index
- [func nameOfSlideshowItem(at: Int) -> String!](ikslideshowdatasource/nameofslideshowitem(at:).md)
  Returns the display name for item at the specified index.
- [func canExportSlideshowItem(at: Int, toApplication: String!) -> Bool](ikslideshowdatasource/canexportslideshowitem(at:toapplication:).md)
  Reports whether the export button should be enabled for a slideshow item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/numberofslideshowitems())*