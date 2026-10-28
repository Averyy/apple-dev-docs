# animationDelay

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the delay, in seconds, between animation steps for an indeterminate progress indicator.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Progress indicators no longer allow the animation delay to be set.

## Declaration

```objc
- (NSTimeInterval) animationDelay;
```

## Return Value

The delay between animation steps. By default, the animation delay is set to 1/12 of a second (5.0/60.0). A determinate progress indicator does not use the animation delay value.

## See Also

### Deprecated methods
- [- animate:](./animate_.md)
  This action method advances the progress animation of an indeterminate progress animator by one step.
- [- setAnimationDelay:](./setanimationdelay_.md)
  Sets the delay, in seconds, between animation steps for an indeterminate progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/animationdelay)*