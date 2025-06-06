# whenLocal(_:)

**Framework**: Distributed  
**Kind**: method

Executes the passed ‘body’ only when the distributed actor is local instance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func whenLocal<T, E>(_ body: (isolated Self) async throws(E) -> T) async throws(E) -> T? where T : Sendable, E : Error
```

#### Discussion

The `Self` passed to the body closure is isolated, meaning that the closure can be used to call non-distributed functions, or even access actor state.

When the actor is remote, the closure won’t be executed and this function will return nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactor/whenlocal(_:))*