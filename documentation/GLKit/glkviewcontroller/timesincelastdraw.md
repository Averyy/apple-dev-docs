# timeSinceLastDraw

**Framework**: GLKit  
**Kind**: property

The amount of time that has passed since the last time the view controller called the view’s [`display()`](glkview/display().md) method.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var timeSinceLastDraw: TimeInterval { get }
```

## See Also

- [var framesDisplayed: Int](glkviewcontroller/framesdisplayed.md)
  The number of frame updates that have been sent by the view controller since it was created.
- [var timeSinceFirstResume: TimeInterval](glkviewcontroller/timesincefirstresume.md)
  The amount of time that has passed since first time the view controller resumed sending update events.
- [var timeSinceLastResume: TimeInterval](glkviewcontroller/timesincelastresume.md)
  The amount of time that has passed since the last time the view controller resumed sending update events.
- [var timeSinceLastUpdate: TimeInterval](glkviewcontroller/timesincelastupdate.md)
  The amount of time that has passed since the last time the view controller called the delegate’s [`glkViewControllerUpdate(_:)`](glkviewcontrollerdelegate/glkviewcontrollerupdate(_:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller/timesincelastdraw)*