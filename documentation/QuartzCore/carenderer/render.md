# render()

**Framework**: Core Animation  
**Kind**: method

Render the update region of the current frame to the target context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func render()
```

## See Also

- [func beginFrame(atTime: CFTimeInterval, timeStamp: UnsafeMutablePointer<CVTimeStamp>?)](carenderer/beginframe(attime:timestamp:).md)
  Begin rendering a frame at the specified time.
- [func updateBounds() -> CGRect](carenderer/updatebounds.md)
  Returns the bounds of the update region that contains all pixels that will be rendered by the current frame.
- [func addUpdate(CGRect)](carenderer/addupdate(_:).md)
  Adds the rectangle to the update region of the current frame.
- [func nextFrameTime() -> CFTimeInterval](carenderer/nextframetime.md)
  Returns the time at which the next update should happen.
- [func endFrame()](carenderer/endframe.md)
  Release any data associated with the current frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/carenderer/render())*