# startAnimation(_:)

**Framework**: AppKit  
**Kind**: method

Starts the animation of an indeterminate progress indicator.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func startAnimation(_ sender: Any?)
```

#### Discussion

Does nothing for a determinate progress indicator.

## Parameters

- `sender`: The object sending the message.

## See Also

- [Progress Indicator Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgIndic/ProgIndic.html#//apple_ref/doc/uid/10000024i)
- [func stopAnimation(Any?)](nsprogressindicator/stopanimation(_:).md)
  Stops the animation of an indeterminate progress indicator.
- [var usesThreadedAnimation: Bool](nsprogressindicator/usesthreadedanimation.md)
  A Boolean that indicates whether the progress indicator implements animation in a separate thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/startanimation(_:))*