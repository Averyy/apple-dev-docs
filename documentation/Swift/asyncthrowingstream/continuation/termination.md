# AsyncThrowingStream.Continuation.Termination

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
- [AsyncThrowingStream.Continuation.Termination.finished(_:)](./termination/finished%28_%29.md)
  The stream finished as a result of calling the continuation’s `finish` method.
- [AsyncThrowingStream.Continuation.Termination.cancelled](./termination/cancelled.md)
  The stream finished as a result of cancellation.

## Relationships

### Conforms To
- [Sendable](../../sendable.md)
- [SendableMetatype](../../sendablemetatype.md)

## See Also

### Handling Termination
- [var onTermination: ((AsyncThrowingStream<Element, Failure>.Continuation.Termination) -> Void)?](./ontermination.md)
  A callback to invoke when canceling iteration of an asynchronous stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/termination)*