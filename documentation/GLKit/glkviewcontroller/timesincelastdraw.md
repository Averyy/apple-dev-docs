# timeSinceLastDraw

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The amount of time that has passed since the last time the view controller called the view’s [`display()`](../glkview/display%28%29.md) method.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var timeSinceLastDraw: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval timeSinceLastDraw;
```

## See Also

### Obtaining Information About View Updates
- [var framesDisplayed: Int](./framesdisplayed.md)
  The number of frame updates that have been sent by the view controller since it was created.
- [var timeSinceFirstResume: TimeInterval](./timesincefirstresume.md)
  The amount of time that has passed since first time the view controller resumed sending update events.
- [var timeSinceLastResume: TimeInterval](./timesincelastresume.md)
  The amount of time that has passed since the last time the view controller resumed sending update events.
- [var timeSinceLastUpdate: TimeInterval](./timesincelastupdate.md)
  The amount of time that has passed since the last time the view controller called the delegate’s [`glkViewControllerUpdate(_:)`](../glkviewcontrollerdelegate/glkviewcontrollerupdate%28_%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller/timesincelastdraw)*