# usesThreadedAnimation

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the progress indicator implements animation in a separate thread.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var usesThreadedAnimation: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), animation of the progress indicator occurs in a separate thread.

If the app becomes multithreaded as a result of an invocation of this method, the app’s performance could become noticeably slower.

## See Also

- [func startAnimation(Any?)](nsprogressindicator/startanimation(_:).md)
  Starts the animation of an indeterminate progress indicator.
- [func stopAnimation(Any?)](nsprogressindicator/stopanimation(_:).md)
  Stops the animation of an indeterminate progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/usesthreadedanimation)*