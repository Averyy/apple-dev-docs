# stopAnimation(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Stops the animation of an indeterminate progress indicator.

**Availability**:
- macOS

## Declaration

```swift
func stopAnimation(_ sender: Any?)
```

```objc
- (void) stopAnimation:(id) sender;
```

## Discussion

Does nothing for a determinate progress indicator.

## Parameters

- `sender`: The object sending the message.

## See Also

### Animating the progress indicator
- [func startAnimation(Any?)](./startanimation%28_%29.md)
  Starts the animation of an indeterminate progress indicator.
- [var usesThreadedAnimation: Bool](./usesthreadedanimation.md)
  A Boolean that indicates whether the progress indicator implements animation in a separate thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/stopanimation(_:))*