# stopAnimation(_:)

**Framework**: AppKit  
**Kind**: method

Stops the animation of an indeterminate progress indicator.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func stopAnimation(_ sender: Any?)
```

#### Discussion

Does nothing for a determinate progress indicator.

## Parameters

- `sender`: The object sending the message.

## See Also

- [func startAnimation(Any?)](nsprogressindicator/startanimation(_:).md)
  Starts the animation of an indeterminate progress indicator.
- [var usesThreadedAnimation: Bool](nsprogressindicator/usesthreadedanimation.md)
  A Boolean that indicates whether the progress indicator implements animation in a separate thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/stopanimation(_:))*