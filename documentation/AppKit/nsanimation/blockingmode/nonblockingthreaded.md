# NSAnimation.BlockingMode.nonblockingThreaded

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Requests the animation to run in a separate thread that is spawned by the `NSAnimation` object.

**Availability**:
- macOS

## Declaration

```swift
case nonblockingThreaded
```

```c
NSAnimationNonblockingThreaded
```

#### Discussion

The secondary thread has its own run loop.

## See Also

### Constants
- [NSAnimation.BlockingMode.blocking](./blocking.md)
  Requests the animation to run in the main thread in a custom run-loop mode that blocks user input.
- [NSAnimation.BlockingMode.nonblocking](./nonblocking.md)
  Requests the animation to run in a standard or specified run-loop mode that allows user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/blockingmode/nonblockingthreaded)*