# reduce(into:_:)

**Framework**: Swift  
**Kind**: method

Returns the result of combining the elements of the sequence using the given closure.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func reduce<Result>(into initialResult: Result, _ updateAccumulatingResult: (inout Result, Self.Element) throws -> ()) rethrows -> Result
```

#### Return Value

The final accumulated value. If the sequence has no elements, the result is `initialResult`.

#### Discussion

Use the `reduce(into:_:)` method to produce a single value from the elements of an entire sequence. For example, you can use this method on an array of integers to filter adjacent equal entries or count frequencies.

This method is preferred over `reduce(_:_:)` for efficiency when the result is a copy-on-write type, for example an Array or a Dictionary.

The `updateAccumulatingResult` closure is called sequentially with a mutable accumulating value initialized to `initialResult` and each element of the sequence. This example shows how to build a dictionary of letter frequencies of a string.

```swift
let letters = "abracadabra"
let letterCount = letters.reduce(into: [:]) { counts, letter in
    counts[letter, default: 0] += 1
}
// letterCount == ["a": 5, "b": 2, "r": 2, "c": 1, "d": 1]
```

When `letters.reduce(into:_:)` is called, the following steps occur:

1. The `updateAccumulatingResult` closure is called with the initial accumulating value—`[:]` in this case—and the first character of `letters`, modifying the accumulating value by setting `1` for the key `"a"`.
2. The closure is called again repeatedly with the updated accumulating value and each element of the sequence.
3. When the sequence is exhausted, the accumulating value is returned to the caller.

If the sequence has no elements, `updateAccumulatingResult` is never executed and `initialResult` is the result of the call to `reduce(into:_:)`.

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## Parameters

- `initialResult`: The value to use as the initial accumulating value.
- `updateAccumulatingResult`: A closure that updates the accumulating   value with an element of the sequence.

## See Also

- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](set/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](set/flatmap(_:)-i3my.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](set/flatmap(_:)-6chuh.md)
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](set/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func sorted() -> [Self.Element]](set/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](set/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](set/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](set/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [var lazy: LazySequence<Self>](set/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/reduce(into:_:))*