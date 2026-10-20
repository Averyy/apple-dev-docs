# autoPlayDelay

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Controls the interval of time before a slideshow starts to play automatically.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var autoPlayDelay: TimeInterval { get set }
```

```objc
@property NSTimeInterval autoPlayDelay;
```

## See Also

### Running and Stopping a Slideshow
- [func run(with: (any IKSlideshowDataSource)!, inMode: String!, options: [AnyHashable : Any]!)](./run%28with,inmode,options%29.md)
  Runs a slideshow that contains the specified kind of items, provided from a data source.
- [func stop(Any!)](./stop%28_%29.md)
  Stops a slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshow/autoplaydelay)*