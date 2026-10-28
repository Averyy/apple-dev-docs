# numberOfSlideshowItems()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the number of items in a slideshow.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func numberOfSlideshowItems() -> Int
```

```objc
- (NSUInteger) numberOfSlideshowItems;
```

## Return Value

The number of items in the slideshow.

## Discussion

Your data source must implement this method.

## See Also

### Providing Slideshow Information
- [func slideshowItem(at: Int) -> Any!](./slideshowitem%28at%29.md)
  Returns the item for a given index
- [func nameOfSlideshowItem(at: Int) -> String!](./nameofslideshowitem%28at%29.md)
  Returns the display name for item at the specified index.
- [func canExportSlideshowItem(at: Int, toApplication: String!) -> Bool](./canexportslideshowitem%28at,toapplication%29.md)
  Reports whether the export button should be enabled for a slideshow item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/numberofslideshowitems())*