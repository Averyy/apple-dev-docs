# slideshowWillStart()

**Framework**: Quartz  
**Kind**: method

Performs custom tasks when the slideshow is about to start.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func slideshowWillStart()
```

#### Discussion

Image Kit invokes this method when the slideshow is about to start. Implement this method to perform custom tasks at that time.

## See Also

- [protocol IKSlideshowDataSource](ikslideshowdatasource.md)
  The `IKSlideshowDataSource` protocol describes the methods that an [`IKSlideshow`](ikslideshow.md) object uses to access the contents of its data source object.
- [func slideshowDidStop()](ikslideshowdatasource/slideshowdidstop.md)
  Performs custom tasks when the slideshow stops.
- [func slideshowDidChangeCurrentIndex(Int)](ikslideshowdatasource/slideshowdidchangecurrentindex(_:).md)
  Performs custom tasks when the slideshow changes to the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/slideshowwillstart())*