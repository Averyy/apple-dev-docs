# preferredFramesPerSecond

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The rate you want the view controller to call the view to update the contents of the view.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var preferredFramesPerSecond: Int { get set }
```

```objc
@property (nonatomic) NSInteger preferredFramesPerSecond;
```

#### Discussion

When your application sets its preferred frame rate, the view controller chooses a frame rate as close to that as possible based on the capabilities of the screen the view is displayed on. The actual frame rate chosen is usually a factor of the maximum refresh rate of the screen to provide a consistent frame rate. For example, if the maximum refresh rate of the screen is `60` frames per second, that is also the highest frame rate the view controller sets as the actual frame rate. However, if you ask for a lower frame rate, it might choose `30`, `20`, `15` or some other factor to be the actual frame rate.

Your application should choose a frame rate that it can consistently maintain.

The default value is `30` frames per second.

## See Also

### Configuring the Frame rate
- [var framesPerSecond: Int](./framespersecond.md)
  The actual rate that the view controller attempts to call the view to update its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller/preferredframespersecond)*