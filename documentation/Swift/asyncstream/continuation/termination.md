# AsyncStream.Continuation.Termination

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

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

## Overview

The `onTermination` closure receives an instance of this type.

## Topics

### Termination States
- [AsyncStream.Continuation.Termination.finished](./termination/finished.md)
  The stream finished as a result of calling the continuation’s `finish` method.
- [AsyncStream.Continuation.Termination.cancelled](./termination/cancelled.md)
  The stream finished as a result of cancellation.
### Hashing
- [var hashValue: Int](./termination/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](./termination/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing Termination Values
- [static func == (AsyncStream<Element>.Continuation.Termination, AsyncStream<Element>.Continuation.Termination) -> Bool](./termination/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (borrowing Self, borrowing Self) -> Bool](./termination/noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](./termination/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../equatable.md)
- [Hashable](../../hashable.md)
- [Sendable](../../sendable.md)
- [SendableMetatype](../../sendablemetatype.md)

## See Also

### Handling Termination
- [var onTermination: ((AsyncStream<Element>.Continuation.Termination) -> Void)?](./ontermination.md)
  A callback to invoke when canceling iteration of an asynchronous stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation/termination)*