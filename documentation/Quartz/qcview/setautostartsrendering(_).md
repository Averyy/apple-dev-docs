# setAutostartsRendering(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets whether the composition that is in the view starts rendering automatically when the view is put on the screen.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setAutostartsRendering(_ flag: Bool)
```

```objc
- (void) setAutostartsRendering:(BOOL) flag;
```

## Parameters

- `flag`: Pass [`true`](../../Swift/true.md) to enable autostart mode; [`false`](../../Swift/false.md) otherwise.

## See Also

### Managing Rendering
- [func startRendering() -> Bool](./startrendering%28%29.md)
  Starts rendering the composition that is in the view.
- [func isRendering() -> Bool](./isrendering%28%29.md)
  Checks whether a composition is rendering in the view.
- [func autostartsRendering() -> Bool](./autostartsrendering%28%29.md)
  Checks whether the view is set to start rendering automatically.
- [func stopRendering()](./stoprendering%28%29.md)
  Stops rendering the composition that is in the view.
- [func pauseRendering()](./pauserendering%28%29.md)
  Pauses rendering in the view.
- [func isPausedRendering() -> Bool](./ispausedrendering%28%29.md)
  Returns whether or not the rendering in the view is paused.
- [func resumeRendering()](./resumerendering%28%29.md)
  Resumes rendering a paused composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/setautostartsrendering(_:))*