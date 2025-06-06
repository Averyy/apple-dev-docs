# drop(while:)

**Framework**: Swift  
**Kind**: method

Omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.

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
func drop(while predicate: @escaping (Self.Element) async throws -> Bool) -> AsyncThrowingDropWhileSequence<Self>
```

#### Return Value

An asynchronous sequence that skips over values until the provided closure returns `false` or throws an error.

#### Discussion

Use `drop(while:)` to omit elements from an asynchronous sequence until the element received meets a condition you specify. If the closure you provide throws an error, the sequence produces no elements and throws the error instead.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The predicate passed to the `drop(while:)` method throws an error if it encounters an even number, and otherwise returns `true` while it receives elements less than `5`. Because the predicate throws when it receives `2` from the base sequence, this example throws without ever printing anything.

```swift
do {
    let stream = Counter(howHigh: 10)
        .drop {
            if $0 % 2 == 0 {
                throw EvenError()
            }
            return $0 < 5
        }
    for try await number in stream {
        print(number)
    }
} catch {
    print(error)
}
// Prints "EvenError()"
```

After the predicate returns `false`, the sequence never executes it again, and from then on the sequence passes through elements from its underlying sequence. A predicate that throws an error also never executes again.

## Parameters

- `predicate`: An error-throwing closure that takes an element as   a parameter and returns a Boolean value indicating whether to drop the   element from the modified sequence.

## See Also

- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](asyncsequence/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [struct AsyncDropFirstSequence](asyncdropfirstsequence.md)
  An asynchronous sequence which omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](asyncsequence/drop(while:)-9sp3b.md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [struct AsyncDropWhileSequence](asyncdropwhilesequence.md)
  An asynchronous sequence which omits elements from the base sequence until a given closure returns false, after which it passes through all remaining elements.
- [struct AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md)
  An asynchronous sequence which omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](asyncsequence/filter(_:)-435af.md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [struct AsyncFilterSequence](asyncfiltersequence.md)
  An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy a given predicate.
- [func filter((Self.Element) async throws -> Bool) -> AsyncThrowingFilterSequence<Self>](asyncsequence/filter(_:)-2cc0l.md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
- [struct AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md)
  An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/drop(while:)-67kgo)*