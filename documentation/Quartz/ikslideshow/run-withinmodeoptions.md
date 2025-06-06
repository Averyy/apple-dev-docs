# run(with:inMode:options:)

**Framework**: Quartz  
**Kind**: method

Runs a slideshow that contains the specified kind of items, provided from a data source.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func run(with dataSource: (any IKSlideshowDataSource)!, inMode slideshowMode: String!, options slideshowOptions: [AnyHashable : Any]! = [:])
```

## Parameters

- `dataSource`: The data source to use for the slideshow.
- `slideshowMode`: A constant that indicate what kind of items are in the slideshow— ,  , or  . See  .
- `slideshowOptions`: A dictionary of slideshow options. See  .

## See Also

- [func stop(Any!)](ikslideshow/stop(_:).md)
  Stops a slideshow.
- [var autoPlayDelay: TimeInterval](ikslideshow/autoplaydelay.md)
  Controls the interval of time before a slideshow starts to play automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshow/run(with:inmode:options:))*