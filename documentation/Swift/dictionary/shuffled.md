# shuffled()

**Framework**: Swift  
**Kind**: method

Returns the elements of the sequence, shuffled.

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
func shuffled() -> [Self.Element]
```

#### Return Value

A shuffled array of this sequence’s elements.

#### Discussion

For example, you can shuffle the numbers between `0` and `9` by calling the `shuffled()` method on that range:

```swift
let numbers = 0...9
let shuffledNumbers = numbers.shuffled()
// shuffledNumbers == [1, 7, 6, 2, 8, 9, 4, 3, 5, 0]
```

This method is equivalent to calling `shuffled(using:)`, passing in the system’s default random generator.

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## See Also

- [func mapValues<T>((Value) throws -> T) rethrows -> Dictionary<Key, T>](dictionary/mapvalues(_:).md)
  Returns a new dictionary containing the keys of this dictionary with the values transformed by the given closure.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](dictionary/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](dictionary/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dictionary/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compactMapValues<T>((Value) throws -> T?) rethrows -> Dictionary<Key, T>](dictionary/compactmapvalues(_:).md)
  Returns a new dictionary containing only the key-value pairs that have non-`nil` values as the result of transformation by the given closure.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](dictionary/flatmap(_:)-i3ly.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dictionary/flatmap(_:)-6chv9.md)
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](dictionary/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled<T>(using: inout T) -> [Self.Element]](dictionary/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/shuffled())*