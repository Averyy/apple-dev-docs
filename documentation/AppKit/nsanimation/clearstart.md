# clearStart()

**Framework**: AppKit  
**Kind**: method

Clears linkage to another animation that causes the receiver to start.

**Availability**:
- macOS ?+

## Declaration

```swift
func clearStart()
```

#### Discussion

The linkage to the other animation is made with [`start(when:reachesProgress:)`](nsanimation/start(when:reachesprogress:).md).

## See Also

- [func start()](nsanimation/start.md)
  Starts the animation represented by the receiver.
- [func start(when: NSAnimation, reachesProgress: NSAnimation.Progress)](nsanimation/start(when:reachesprogress:).md)
  Starts running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func stop(when: NSAnimation, reachesProgress: NSAnimation.Progress)](nsanimation/stop(when:reachesprogress:).md)
  Stops running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func clearStop()](nsanimation/clearstop.md)
  Clears linkage to another animation that causes the receiver to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/clearstart())*