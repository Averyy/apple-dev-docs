# stop(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Stops a slideshow.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func stop(_ sender: Any!)
```

```objc
- (void) stopSlideshow:(id) sender;
```

## Discussion

This method is invoked when the user clicks a button or issues a stop command.

## Parameters

- `sender`: The object sending the message to stop the slideshow.

## See Also

### Running and Stopping a Slideshow
- [func run(with: (any IKSlideshowDataSource)!, inMode: String!, options: [AnyHashable : Any]!)](./run%28with,inmode,options%29.md)
  Runs a slideshow that contains the specified kind of items, provided from a data source.
- [var autoPlayDelay: TimeInterval](./autoplaydelay.md)
  Controls the interval of time before a slideshow starts to play automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshow/stop(_:))*