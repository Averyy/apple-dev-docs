# slideshowItem(at:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the item for a given index

**Availability**:
- macOS 10.4+

## Declaration

```swift
func slideshowItem(at index: Int) -> Any!
```

#### Return Value

The object that corresponds to the item at the specified index. The item can be any of the following objects: [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage), [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) (to specify a path name), [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL), [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper), [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage), or [`PDFPage`](https://developer.apple.com/documentation/PDFKit/PDFPage).

#### Discussion

Your data source must implement this method.

## Parameters

- `index`: An index of an item in the slideshow.

## See Also

- [func numberOfSlideshowItems() -> Int](ikslideshowdatasource/numberofslideshowitems.md)
  Returns the number of items in a slideshow.
- [func nameOfSlideshowItem(at: Int) -> String!](ikslideshowdatasource/nameofslideshowitem(at:).md)
  Returns the display name for item at the specified index.
- [func canExportSlideshowItem(at: Int, toApplication: String!) -> Bool](ikslideshowdatasource/canexportslideshowitem(at:toapplication:).md)
  Reports whether the export button should be enabled for a slideshow item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/slideshowitem(at:))*