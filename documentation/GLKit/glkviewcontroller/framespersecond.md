# framesPerSecond

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The actual rate that the view controller attempts to call the view to update its contents.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var framesPerSecond: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger framesPerSecond;
```

## Discussion

The view controller attempts to maintain this frame rate, but it may still drop frames if the per-frame processing performed by your application takes more time than the time between frames.

## See Also

### Configuring the Frame rate
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The rate you want the view controller to call the view to update the contents of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller/framespersecond)*