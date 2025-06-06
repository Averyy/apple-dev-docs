# slideshowDidStop()

**Framework**: Quartz  
**Kind**: method

Performs custom tasks when the slideshow stops.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func slideshowDidStop()
```

#### Discussion

TImage Kit invokes this method when the slideshow stops. Implement this method to perform custom tasks at that time.

## See Also

- [protocol IKSlideshowDataSource](ikslideshowdatasource.md)
  The `IKSlideshowDataSource` protocol describes the methods that an [`IKSlideshow`](ikslideshow.md) object uses to access the contents of its data source object.
- [func slideshowWillStart()](ikslideshowdatasource/slideshowwillstart.md)
  Performs custom tasks when the slideshow is about to start.
- [func slideshowDidChangeCurrentIndex(Int)](ikslideshowdatasource/slideshowdidchangecurrentindex(_:).md)
  Performs custom tasks when the slideshow changes to the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/slideshowdidstop())*