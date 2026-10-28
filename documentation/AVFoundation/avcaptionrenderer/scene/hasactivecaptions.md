# hasActiveCaptions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the scene contains one or more active captions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var hasActiveCaptions: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasActiveCaptions;
```

## Discussion

Knowing when the renderer has active captions can be useful to scrub to times where captions are present, or skip scenes where no captions exist.

> ❗ **Important**:  Don’t use this property value to restrict drawing. Instead, draw an empty fill in [`render(in:for:)`](../render%28in,for%29.md) when there aren’t active captions to render.

## See Also

### Inspecting the scene
- [var timeRange: CMTimeRange](./timerange.md)
  The time range during which the system doesn’t modify the scene.
- [var needsPeriodicRefresh: Bool](./needsperiodicrefresh.md)
  A Boolean value that indicates whether the scene requires redrawing while your app progresses through the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/scene/hasactivecaptions)*