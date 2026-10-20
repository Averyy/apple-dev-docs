# stop(when:reachesProgress:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Stops running the animation represented by the receiver when another animation reaches a specific progress mark.

**Availability**:
- macOS

## Declaration

```swift
func stop(when animation: NSAnimation, reachesProgress stopProgress: NSAnimation.Progress)
```

```objc
- (void) stopWhenAnimation:(NSAnimation *) animation reachesProgress:(NSAnimationProgress) stopProgress;
```

#### Discussion

This method links the running of two animations together. You can set only one `NSAnimation` object as a start animation and one as a stop animation at any one time. Setting a new stop animation removes any animation previously set.

## Parameters

- `animation`: The other `NSAnimation` object with which the receiver is linked.
- `stopProgress`: A `float` value (typed as NSAnimationProgress) that specifies a progress mark of the other animation.

## See Also

### Related Documentation
- [func stop()](./stop%28%29.md)
  Stops the animation represented by the receiver.
### Linking Animations Together
- [func start(when: NSAnimation, reachesProgress: NSAnimation.Progress)](./start%28when,reachesprogress%29.md)
  Starts running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func clearStart()](./clearstart%28%29.md)
  Clears linkage to another animation that causes the receiver to start.
- [func clearStop()](./clearstop%28%29.md)
  Clears linkage to another animation that causes the receiver to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/stop(when:reachesprogress:))*