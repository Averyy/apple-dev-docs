# nameOfSlideshowItem(at:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the display name for item at the specified index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func nameOfSlideshowItem(at index: Int) -> String!
```

```objc
- (NSString *) nameOfSlideshowItemAtIndex:(NSUInteger) index;
```

## Return Value

The display name. For the best user experience, you should provide the localized name, because this string appears in the user interface.

## Discussion

This method is optional.

## Parameters

- `index`: The index for a slideshow item.

## See Also

### Providing Slideshow Information
- [func numberOfSlideshowItems() -> Int](./numberofslideshowitems%28%29.md)
  Returns the number of items in a slideshow.
- [func slideshowItem(at: Int) -> Any!](./slideshowitem%28at%29.md)
  Returns the item for a given index
- [func canExportSlideshowItem(at: Int, toApplication: String!) -> Bool](./canexportslideshowitem%28at,toapplication%29.md)
  Reports whether the export button should be enabled for a slideshow item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/nameofslideshowitem(at:))*