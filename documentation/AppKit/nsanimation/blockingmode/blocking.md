# NSAnimation.BlockingMode.blocking

**Framework**: AppKit  
**Kind**: case

Requests the animation to run in the main thread in a custom run-loop mode that blocks user input.

**Availability**:
- macOS ?+

## Declaration

```swift
case blocking
```

#### Discussion

This is the default.

## See Also

- [NSAnimation.BlockingMode.nonblocking](nsanimation/blockingmode/nonblocking.md)
  Requests the animation to run in a standard or specified run-loop mode that allows user input.
- [NSAnimation.BlockingMode.nonblockingThreaded](nsanimation/blockingmode/nonblockingthreaded.md)
  Requests the animation to run in a separate thread that is spawned by the `NSAnimation` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/blockingmode/blocking)*