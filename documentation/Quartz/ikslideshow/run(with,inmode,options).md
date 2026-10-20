# run(with:inMode:options:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Runs a slideshow that contains the specified kind of items, provided from a data source.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func run(with dataSource: (any IKSlideshowDataSource)!, inMode slideshowMode: String!, options slideshowOptions: [AnyHashable : Any]! = [:])
```

```objc
- (void) runSlideshowWithDataSource:(id<IKSlideshowDataSource>) dataSource inMode:(NSString *) slideshowMode options:(NSDictionary *) slideshowOptions;
```

## Parameters

- `dataSource`: The data source to use for the slideshow.
- `slideshowMode`: A constant that indicate what kind of items are in the slideshow—`IKSlideshowModeImages`, `IKSlideshowModePDF`, or `IKSlideshowModeQuickLook`. See [Slideshow Modes](../slideshow-modes.md).
- `slideshowOptions`: A dictionary of slideshow options. See [Slideshow Option Keys](../slideshow-option-keys.md).

## See Also

### Running and Stopping a Slideshow
- [func stop(Any!)](./stop%28_%29.md)
  Stops a slideshow.
- [var autoPlayDelay: TimeInterval](./autoplaydelay.md)
  Controls the interval of time before a slideshow starts to play automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshow/run(with:inmode:options:))*