# stopTracking()

**Framework**: ARKit  
**Kind**: method

Stops repeating the raycast query.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func stopTracking()
```

#### Discussion

A tracked raycast updates continuously until you stop it explicitly by calling [`stopTracking()`](artrackedraycast/stoptracking().md). A raycast will automatically stop when:

- ARKit calls [`sessionWasInterrupted(_:)`](arsessionobserver/sessionwasinterrupted(_:).md).
- You change the session’s configuration.
- You deallocate the [`ARTrackedRaycast`](artrackedraycast.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackedraycast/stoptracking())*