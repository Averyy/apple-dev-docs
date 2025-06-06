# clearStop()

**Framework**: AppKit  
**Kind**: method

Clears linkage to another animation that causes the receiver to stop.

**Availability**:
- macOS ?+

## Declaration

```swift
func clearStop()
```

#### Discussion

The linkage to the other animation is made with [`stop(when:reachesProgress:)`](nsanimation/stop(when:reachesprogress:).md).

## See Also

- [func stop()](nsanimation/stop.md)
  Stops the animation represented by the receiver.
- [func start(when: NSAnimation, reachesProgress: NSAnimation.Progress)](nsanimation/start(when:reachesprogress:).md)
  Starts running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func stop(when: NSAnimation, reachesProgress: NSAnimation.Progress)](nsanimation/stop(when:reachesprogress:).md)
  Stops running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func clearStart()](nsanimation/clearstart.md)
  Clears linkage to another animation that causes the receiver to start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/clearstop())*