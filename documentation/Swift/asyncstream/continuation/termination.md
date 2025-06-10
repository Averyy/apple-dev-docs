# AsyncStream.Continuation.Termination

**Framework**: Swift  
**Kind**: enum

A type that indicates how the stream terminated.

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
enum Termination
```

#### Overview

The `onTermination` closure receives an instance of this type.

## Topics

### Termination States
- [AsyncStream.Continuation.Termination.finished](asyncstream/continuation/termination/finished.md)
  The stream finished as a result of calling the continuation’s `finish` method.
- [AsyncStream.Continuation.Termination.cancelled](asyncstream/continuation/termination/cancelled.md)
  The stream finished as a result of cancellation.
### Hashing
- [var hashValue: Int](asyncstream/continuation/termination/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](asyncstream/continuation/termination/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing Termination Values
- [static func == (AsyncStream<Element>.Continuation.Termination, AsyncStream<Element>.Continuation.Termination) -> Bool](asyncstream/continuation/termination/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](asyncstream/continuation/termination/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](asyncstream/continuation/termination/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [var onTermination: ((AsyncStream<Element>.Continuation.Termination) -> Void)?](asyncstream/continuation/ontermination.md)
  A callback to invoke when canceling iteration of an asynchronous stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation/termination)*