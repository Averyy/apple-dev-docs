# filter(_:)

**Framework**: Swift  
**Kind**: method

Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.

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
@preconcurrency
func filter(_ isIncluded: @escaping (Self.Element) async -> Bool) -> AsyncFilterSequence<Self>
```

#### Return Value

An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.

#### Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `filter(_:)` method returns `true` for even values and `false` for odd values, thereby filtering out the odd values:

```swift
let stream = Counter(howHigh: 10)
    .filter { $0 % 2 == 0 }
for await number in stream {
    print(number, terminator: " ")
}
// Prints "2 4 6 8 10 "
```

## Parameters

- `isIncluded`: A closure that takes an element of the   asynchronous sequence as its argument and returns a Boolean value   that indicates whether to include the element in the filtered sequence.

## See Also

- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](asyncsequence/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [struct AsyncDropFirstSequence](asyncdropfirstsequence.md)
  An asynchronous sequence which omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](asyncsequence/drop(while:)-9sp3b.md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [struct AsyncDropWhileSequence](asyncdropwhilesequence.md)
  An asynchronous sequence which omits elements from the base sequence until a given closure returns false, after which it passes through all remaining elements.
- [func drop(while: (Self.Element) async throws -> Bool) -> AsyncThrowingDropWhileSequence<Self>](asyncsequence/drop(while:)-67kgo.md)
  Omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [struct AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md)
  An asynchronous sequence which omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [struct AsyncFilterSequence](asyncfiltersequence.md)
  An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy a given predicate.
- [func filter((Self.Element) async throws -> Bool) -> AsyncThrowingFilterSequence<Self>](asyncsequence/filter(_:)-2cc0l.md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
- [struct AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md)
  An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/filter(_:)-435af)*