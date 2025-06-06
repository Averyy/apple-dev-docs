# stop(when:reachesProgress:)

**Framework**: AppKit  
**Kind**: method

Stops running the animation represented by the receiver when another animation reaches a specific progress mark.

**Availability**:
- macOS ?+

## Declaration

```swift
func stop(when animation: NSAnimation, reachesProgress stopProgress: NSAnimation.Progress)
```

#### Discussion

This method links the running of two animations together. You can set only one `NSAnimation` object as a start animation and one as a stop animation at any one time. Setting a new stop animation removes any animation previously set.

## Parameters

- `animation`: The other   object with which the receiver is linked.
- `stopProgress`: A   value (typed as NSAnimationProgress) that specifies a progress mark of the other animation.

## See Also

- [func stop()](nsanimation/stop.md)
  Stops the animation represented by the receiver.
- [func start(when: NSAnimation, reachesProgress: NSAnimation.Progress)](nsanimation/start(when:reachesprogress:).md)
  Starts running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func clearStart()](nsanimation/clearstart.md)
  Clears linkage to another animation that causes the receiver to start.
- [func clearStop()](nsanimation/clearstop.md)
  Clears linkage to another animation that causes the receiver to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/stop(when:reachesprogress:))*