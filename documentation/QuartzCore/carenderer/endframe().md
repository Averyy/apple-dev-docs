# endFrame()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Release any data associated with the current frame.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func endFrame()
```

```objc
- (void) endFrame;
```

## See Also

### Rendering a Frame
- [func beginFrame(atTime: CFTimeInterval, timeStamp: UnsafeMutablePointer<CVTimeStamp>?)](./beginframe%28attime,timestamp%29.md)
  Begin rendering a frame at the specified time.
- [func updateBounds() -> CGRect](./updatebounds%28%29.md)
  Returns the bounds of the update region that contains all pixels that will be rendered by the current frame.
- [func addUpdate(CGRect)](./addupdate%28_%29.md)
  Adds the rectangle to the update region of the current frame.
- [func render()](./render%28%29.md)
  Render the update region of the current frame to the target context.
- [func nextFrameTime() -> CFTimeInterval](./nextframetime%28%29.md)
  Returns the time at which the next update should happen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/carenderer/endframe())*