# start(when:reachesProgress:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Starts running the animation represented by the receiver when another animation reaches a specific progress mark.

**Availability**:
- macOS

## Declaration

```swift
func start(when animation: NSAnimation, reachesProgress startProgress: NSAnimation.Progress)
```

```objc
- (void) startWhenAnimation:(NSAnimation *) animation reachesProgress:(NSAnimationProgress) startProgress;
```

## Discussion

This method links the running of two animations together. You can set only one `NSAnimation` object as a start animation and one as a stop animation at any one time. Setting a new start animation removes any animation previously set.

## Parameters

- `animation`: The other `NSAnimation` object with which the receiver is linked.
- `startProgress`: A `float` value (typed as NSAnimationProgress) that specifies a progress mark of the other animation.

## See Also

### Related Documentation
- [func start()](./start%28%29.md)
  Starts the animation represented by the receiver.
### Linking Animations Together
- [func stop(when: NSAnimation, reachesProgress: NSAnimation.Progress)](./stop%28when,reachesprogress%29.md)
  Stops running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func clearStart()](./clearstart%28%29.md)
  Clears linkage to another animation that causes the receiver to start.
- [func clearStop()](./clearstop%28%29.md)
  Clears linkage to another animation that causes the receiver to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/start(when:reachesprogress:))*