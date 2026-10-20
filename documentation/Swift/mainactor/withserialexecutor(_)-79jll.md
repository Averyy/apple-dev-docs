# withSerialExecutor(_:)

**Framework**: Swift  
**Kind**: method

Perform an operation with the actor’s [`SerialExecutor`](serialexecutor.md).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func withSerialExecutor<T, E>(_ operation: (any SerialExecutor) throws(E) -> T) throws(E) -> T where E : Error, T : ~Copyable
```

#### Discussion

This converts the actor’s [`unownedExecutor`](actor/unownedexecutor.md) to a [`SerialExecutor`](serialexecutor.md) while retaining the actor for the duration of the operation. This is to ensure the lifetime of the executor while performing the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mainactor/withserialexecutor(_:)-79jll)*