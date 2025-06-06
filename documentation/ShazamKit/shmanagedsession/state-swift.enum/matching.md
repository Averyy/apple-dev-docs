# SHManagedSession.State.matching

**Framework**: ShazamKit  
**Kind**: case

The session is recording and making at least one match attempt.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case matching
```

#### Discussion

When a session is in this state, the framework ignores calls to [`prepare()`](shmanagedsession/prepare().md).

## See Also

- [SHManagedSession.State.idle](shmanagedsession/state-swift.enum/idle.md)
  The session isn’t recording or making a match attempt.
- [SHManagedSession.State.prerecording](shmanagedsession/state-swift.enum/prerecording.md)
  The session has the resources it needs for matching and is prerecording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmanagedsession/state-swift.enum/matching)*