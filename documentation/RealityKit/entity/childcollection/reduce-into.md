# reduce(into:_:)

**Framework**: RealityKit  
**Kind**: method

Returns the result of combining the elements of the sequence using the given closure.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

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

```None
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

- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](entity/childcollection/map(_:)-78ywb.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](entity/childcollection/flatmap(_:)-5ijyo.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](entity/childcollection/flatmap(_:)-9ovg6.md)
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](entity/childcollection/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](entity/childcollection/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](entity/childcollection/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/reduce(into:_:))*