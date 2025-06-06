# prefix(_:)

**Framework**: Swift  
**Kind**: method

Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.

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
func prefix(_ count: Int) -> AsyncPrefixSequence<Self>
```

#### Return Value

An asynchronous sequence starting at the beginning of the base sequence with at most `count` elements.

#### Discussion

Use `prefix(_:)` to reduce the number of elements produced by the asynchronous sequence.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `prefix(_:)` method causes the modified sequence to pass through the first six values, then end.

```swift
for await number in Counter(howHigh: 10).prefix(6) {
    print(number, terminator: " ")
}
// Prints "1 2 3 4 5 6 "
```

If the count passed to `prefix(_:)` exceeds the number of elements in the base sequence, the result contains all of the elements in the sequence.

## Parameters

- `count`: The maximum number of elements to return. The value of    must be greater than or equal to zero.

## See Also

- [struct AsyncPrefixSequence](asyncprefixsequence.md)
  An asynchronous sequence, up to a specified maximum length, containing the initial elements of a base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](asyncsequence/prefix(while:)-2xy95.md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [struct AsyncPrefixWhileSequence](asyncprefixwhilesequence.md)
  An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy a given predicate.
- [func prefix(while: (Self.Element) async throws -> Bool) rethrows -> AsyncThrowingPrefixWhileSequence<Self>](asyncsequence/prefix(while:)-6yp5n.md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
- [struct AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md)
  An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/prefix(_:))*