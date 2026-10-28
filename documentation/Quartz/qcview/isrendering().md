# isRendering()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Checks whether a composition is rendering in the view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func isRendering() -> Bool
```

```objc
- (BOOL) isRendering;
```

## Return Value

Returns [`true`](../../Swift/true.md) if a composition is rendering in the view; [`false`](../../Swift/false.md) otherwise.

## See Also

### Managing Rendering
- [func startRendering() -> Bool](./startrendering%28%29.md)
  Starts rendering the composition that is in the view.
- [func autostartsRendering() -> Bool](./autostartsrendering%28%29.md)
  Checks whether the view is set to start rendering automatically.
- [func setAutostartsRendering(Bool)](./setautostartsrendering%28_%29.md)
  Sets whether the composition that is in the view starts rendering automatically when the view is put on the screen.
- [func stopRendering()](./stoprendering%28%29.md)
  Stops rendering the composition that is in the view.
- [func pauseRendering()](./pauserendering%28%29.md)
  Pauses rendering in the view.
- [func isPausedRendering() -> Bool](./ispausedrendering%28%29.md)
  Returns whether or not the rendering in the view is paused.
- [func resumeRendering()](./resumerendering%28%29.md)
  Resumes rendering a paused composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/isrendering())*