# beginFrame(atTime:timeStamp:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Begin rendering a frame at the specified time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func beginFrame(atTime t: CFTimeInterval, timeStamp ts: UnsafeMutablePointer<CVTimeStamp>?)
```

```objc
- (void) beginFrameAtTime:(CFTimeInterval) t timeStamp:(CVTimeStamp *) ts;
```

## Parameters

- `t`: The layer time.
- `ts`: The display timestamp associated with timeInterval. Can be null.

## See Also

### Rendering a Frame
- [func updateBounds() -> CGRect](./updatebounds%28%29.md)
  Returns the bounds of the update region that contains all pixels that will be rendered by the current frame.
- [func addUpdate(CGRect)](./addupdate%28_%29.md)
  Adds the rectangle to the update region of the current frame.
- [func render()](./render%28%29.md)
  Render the update region of the current frame to the target context.
- [func nextFrameTime() -> CFTimeInterval](./nextframetime%28%29.md)
  Returns the time at which the next update should happen.
- [func endFrame()](./endframe%28%29.md)
  Release any data associated with the current frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/carenderer/beginframe(attime:timestamp:))*