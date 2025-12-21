# withUnsynchronized(_:)

**Framework**: RealityKit  
**Kind**: method

Calls the given closure in a way such that component changes that the closure makes don’t trigger synchronization.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func withUnsynchronized(_ changes: () -> Void)
```

#### Discussion

Use this method to make local changes that don’t affect remote peers, like aligning a billboard component to face the local camera.

Using this method doesn’t permanently prevent changes from being synchronized. If you modify the same components immediately before the call to [`withUnsynchronized(_:)`](hassynchronization/withunsynchronized(_:).md), or anytime afterward, the changes are synchronized.

If the local peer doesn’t own the associated entity, changes that the remote owner makes continue to synchronize, overwriting local, unsynchronized changes.

## Parameters

- `changes`: A closure that the method calls while suppressing   synchronization triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hassynchronization/withunsynchronized(_:))*