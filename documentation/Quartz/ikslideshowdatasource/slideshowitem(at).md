# slideshowItem(at:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the item for a given index

**Availability**:
- macOS 10.4+

## Declaration

```swift
func slideshowItem(at index: Int) -> Any!
```

```objc
- (id) slideshowItemAtIndex:(NSUInteger) index;
```

## Return Value

The object that corresponds to the item at the specified index. The item can be any of the following objects: [`NSImage`](../../AppKit/nsimage.md), [`NSString`](../../Foundation/nsstring.md) (to specify a path name), [`NSURL`](../../Foundation/nsurl.md), [`FileWrapper`](../../Foundation/filewrapper.md), [`CGImage`](../../CoreGraphics/cgimage.md), or [`PDFPage`](../../PDFKit/pdfpage.md).

## Discussion

Your data source must implement this method.

## Parameters

- `index`: An index of an item in the slideshow.

## See Also

### Providing Slideshow Information
- [func numberOfSlideshowItems() -> Int](./numberofslideshowitems%28%29.md)
  Returns the number of items in a slideshow.
- [func nameOfSlideshowItem(at: Int) -> String!](./nameofslideshowitem%28at%29.md)
  Returns the display name for item at the specified index.
- [func canExportSlideshowItem(at: Int, toApplication: String!) -> Bool](./canexportslideshowitem%28at,toapplication%29.md)
  Reports whether the export button should be enabled for a slideshow item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/slideshowitem(at:))*