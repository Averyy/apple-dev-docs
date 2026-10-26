# animate:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This action method advances the progress animation of an indeterminate progress animator by one step.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: `NSProgressIndicator` no longer supports incrementing the animation using this method. Use the [`startAnimation(_:)`](./startanimation%28_%29.md) and [`stopAnimation(_:)`](./stopanimation%28_%29.md) methods to perform animation of the progress indicator.

## Declaration

```objc
- (void) animate:(id) sender;
```

## Parameters

- `sender`: The object sending the message.

## See Also

### Deprecated methods
- [- animationDelay](./animationdelay.md)
  Returns the delay, in seconds, between animation steps for an indeterminate progress indicator.
- [- setAnimationDelay:](./setanimationdelay_.md)
  Sets the delay, in seconds, between animation steps for an indeterminate progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/animate:)*