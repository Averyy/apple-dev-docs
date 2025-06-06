# addUpdate(_:)

**Framework**: Core Animation  
**Kind**: method

Adds the rectangle to the update region of the current frame.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addUpdate(_ r: CGRect)
```

## Parameters

- `r`: A rectangle defining the region to be added to the update region.

## See Also

- [func beginFrame(atTime: CFTimeInterval, timeStamp: UnsafeMutablePointer<CVTimeStamp>?)](carenderer/beginframe(attime:timestamp:).md)
  Begin rendering a frame at the specified time.
- [func updateBounds() -> CGRect](carenderer/updatebounds.md)
  Returns the bounds of the update region that contains all pixels that will be rendered by the current frame.
- [func render()](carenderer/render.md)
  Render the update region of the current frame to the target context.
- [func nextFrameTime() -> CFTimeInterval](carenderer/nextframetime.md)
  Returns the time at which the next update should happen.
- [func endFrame()](carenderer/endframe.md)
  Release any data associated with the current frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/carenderer/addupdate(_:))*