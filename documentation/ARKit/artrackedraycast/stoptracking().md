# stopTracking()

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Stops repeating the raycast query.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
func stopTracking()
```

```objc
- (void) stopTracking;
```

#### Discussion

A tracked raycast updates continuously until you stop it explicitly by calling [`stopTracking()`](./stoptracking%28%29.md). A raycast will automatically stop when:

- ARKit calls [`sessionWasInterrupted(_:)`](../arsessionobserver/sessionwasinterrupted%28_%29.md).
- You change the session’s configuration.
- You deallocate the [`ARTrackedRaycast`](../artrackedraycast.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackedraycast/stoptracking())*