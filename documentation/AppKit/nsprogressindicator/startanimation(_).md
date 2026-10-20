# startAnimation(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Starts the animation of an indeterminate progress indicator.

**Availability**:
- macOS

## Declaration

```swift
func startAnimation(_ sender: Any?)
```

```objc
- (void) startAnimation:(id) sender;
```

#### Discussion

Does nothing for a determinate progress indicator.

## Parameters

- `sender`: The object sending the message.

## See Also

### Related Documentation
- [Progress Indicator Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgIndic/ProgIndic.html#//apple_ref/doc/uid/10000024i)
### Animating the progress indicator
- [func stopAnimation(Any?)](./stopanimation%28_%29.md)
  Stops the animation of an indeterminate progress indicator.
- [var usesThreadedAnimation: Bool](./usesthreadedanimation.md)
  A Boolean that indicates whether the progress indicator implements animation in a separate thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/startanimation(_:))*