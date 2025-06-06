# setAutostartsRendering(_:)

**Framework**: Quartz  
**Kind**: method

Sets whether the composition that is in the view starts rendering automatically when the view is put on the screen.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setAutostartsRendering(_ flag: Bool)
```

## Parameters

- `flag`: Pass   to enable autostart mode;   otherwise.

## See Also

- [func startRendering() -> Bool](qcview/startrendering.md)
  Starts rendering the composition that is in the view.
- [func isRendering() -> Bool](qcview/isrendering.md)
  Checks whether a composition is rendering in the view.
- [func autostartsRendering() -> Bool](qcview/autostartsrendering.md)
  Checks whether the view is set to start rendering automatically.
- [func stopRendering()](qcview/stoprendering.md)
  Stops rendering the composition that is in the view.
- [func pauseRendering()](qcview/pauserendering.md)
  Pauses rendering in the view.
- [func isPausedRendering() -> Bool](qcview/ispausedrendering.md)
  Returns whether or not the rendering in the view is paused.
- [func resumeRendering()](qcview/resumerendering.md)
  Resumes rendering a paused composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/setautostartsrendering(_:))*