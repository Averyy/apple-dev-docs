# framesPerSecond

**Framework**: GLKit  
**Kind**: property

The actual rate that the view controller attempts to call the view to update its contents.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var framesPerSecond: Int { get }
```

#### Discussion

The view controller attempts to maintain this frame rate, but it may still drop frames if the per-frame processing performed by your application takes more time than the time between frames.

## See Also

- [var preferredFramesPerSecond: Int](glkviewcontroller/preferredframespersecond.md)
  The rate you want the view controller to call the view to update the contents of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller/framespersecond)*