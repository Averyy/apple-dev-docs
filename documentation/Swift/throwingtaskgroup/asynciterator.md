# ThrowingTaskGroup.AsyncIterator

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

The type of asynchronous iterator that produces elements of this asynchronous sequence.

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
typealias AsyncIterator = ThrowingTaskGroup<ChildTaskResult, Failure>.Iterator
```

Available when `ChildTaskResult` conforms to `Sendable` and `Failure` conforms to `Error`.

## See Also

### Supporting Types
- [ThrowingTaskGroup.Element](./element.md)
  The type of element produced by this asynchronous sequence.
- [ThrowingTaskGroup.Iterator](./iterator.md)
  A type that provides an iteration interface over the results of tasks added to the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/asynciterator)*