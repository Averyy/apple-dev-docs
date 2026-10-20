# timeRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time range during which the system doesn’t modify the scene.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var timeRange: CMTimeRange { get }
```

```objc
@property (nonatomic, readonly) CMTimeRange timeRange;
```

## See Also

### Inspecting the scene
- [var hasActiveCaptions: Bool](./hasactivecaptions.md)
  A Boolean value that indicates whether the scene contains one or more active captions.
- [var needsPeriodicRefresh: Bool](./needsperiodicrefresh.md)
  A Boolean value that indicates whether the scene requires redrawing while your app progresses through the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/scene/timerange)*