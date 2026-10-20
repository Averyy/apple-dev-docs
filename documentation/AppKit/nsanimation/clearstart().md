# clearStart()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Clears linkage to another animation that causes the receiver to start.

**Availability**:
- macOS

## Declaration

```swift
func clearStart()
```

```objc
- (void) clearStartAnimation;
```

#### Discussion

The linkage to the other animation is made with [`start(when:reachesProgress:)`](./start%28when,reachesprogress%29.md).

## See Also

### Related Documentation
- [func start()](./start%28%29.md)
  Starts the animation represented by the receiver.
### Linking Animations Together
- [func start(when: NSAnimation, reachesProgress: NSAnimation.Progress)](./start%28when,reachesprogress%29.md)
  Starts running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func stop(when: NSAnimation, reachesProgress: NSAnimation.Progress)](./stop%28when,reachesprogress%29.md)
  Stops running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func clearStop()](./clearstop%28%29.md)
  Clears linkage to another animation that causes the receiver to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/clearstart())*