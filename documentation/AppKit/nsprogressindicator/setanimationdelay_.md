# setAnimationDelay:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the delay, in seconds, between animation steps for an indeterminate progress indicator.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Progress indicators no longer allow the animation delay to be set.

## Declaration

```objc
- (void) setAnimationDelay:(NSTimeInterval) delay;
```

## Parameters

- `delay`: The number of seconds between animation steps. By default, the animation delay is set to 1/12 of a second (5.0/60.0). Setting the delay to a double value larger than 5.0/60.0 slows the animation, while setting the delay to a smaller value speeds it up. A determinate progress indicator does not use the animation delay value.

## See Also

### Deprecated methods
- [- animate:](./animate_.md)
  This action method advances the progress animation of an indeterminate progress animator by one step.
- [- animationDelay](./animationdelay.md)
  Returns the delay, in seconds, between animation steps for an indeterminate progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/setanimationdelay:)*