# startRendering()

**Framework**: Quartz  
**Kind**: method

Starts rendering the composition that is in the view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func startRendering() -> Bool
```

#### Return Value

Returns [`false`](https://developer.apple.com/documentation/swift/false) if the composition fails to start rendering; [`true`](https://developer.apple.com/documentation/swift/true) otherwise.

## See Also

- [func isRendering() -> Bool](qcview/isrendering.md)
  Checks whether a composition is rendering in the view.
- [func autostartsRendering() -> Bool](qcview/autostartsrendering.md)
  Checks whether the view is set to start rendering automatically.
- [func setAutostartsRendering(Bool)](qcview/setautostartsrendering(_:).md)
  Sets whether the composition that is in the view starts rendering automatically when the view is put on the screen.
- [func stopRendering()](qcview/stoprendering.md)
  Stops rendering the composition that is in the view.
- [func pauseRendering()](qcview/pauserendering.md)
  Pauses rendering in the view.
- [func isPausedRendering() -> Bool](qcview/ispausedrendering.md)
  Returns whether or not the rendering in the view is paused.
- [func resumeRendering()](qcview/resumerendering.md)
  Resumes rendering a paused composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/startrendering())*