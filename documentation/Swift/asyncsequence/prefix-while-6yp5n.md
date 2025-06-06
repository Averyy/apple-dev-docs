# prefix(while:)

**Framework**: Swift  
**Kind**: method

Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.

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
func prefix(while predicate: @escaping (Self.Element) async throws -> Bool) rethrows -> AsyncThrowingPrefixWhileSequence<Self>
```

#### Return Value

An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate. If the predicate throws an error, the sequence contains only values produced prior to the error.

#### Discussion

Use `prefix(while:)` to produce values while elements from the base sequence meet a condition you specify. The modified sequence ends when the predicate closure returns `false` or throws an error.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `prefix(_:)` method causes the modified sequence to pass through values less than `8`, but throws an error when it receives a value that’s divisible by `5`:

```swift
do {
    let stream = try Counter(howHigh: 10)
        .prefix {
            if $0 % 5 == 0 {
                throw MyError()
            }
            return $0 < 8
        }
    for try await number in stream {
        print(number, terminator: " ")
    }
} catch {
    print("Error: \(error)")
}
// Prints "1 2 3 4 Error: MyError() "
```

## Parameters

- `predicate`: A error-throwing closure that takes an element of   the asynchronous sequence as its argument and returns a Boolean value   that indicates whether to include the element in the modified sequence.

## See Also

- [func prefix(Int) -> AsyncPrefixSequence<Self>](asyncsequence/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [struct AsyncPrefixSequence](asyncprefixsequence.md)
  An asynchronous sequence, up to a specified maximum length, containing the initial elements of a base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](asyncsequence/prefix(while:)-2xy95.md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [struct AsyncPrefixWhileSequence](asyncprefixwhilesequence.md)
  An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy a given predicate.
- [struct AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md)
  An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/prefix(while:)-6yp5n)*