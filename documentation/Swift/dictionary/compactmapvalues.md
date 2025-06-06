# compactMapValues(_:)

**Framework**: Swift  
**Kind**: method

Returns a new dictionary containing only the key-value pairs that have non-`nil` values as the result of transformation by the given closure.

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
func compactMapValues<T>(_ transform: (Value) throws -> T?) rethrows -> Dictionary<Key, T>
```

#### Return Value

A dictionary containing the keys and non-`nil` transformed values of this dictionary.

#### Discussion

Use this method to receive a dictionary with non-optional values when your transformation produces optional values.

In this example, note the difference in the result of using `mapValues` and `compactMapValues` with a transformation that returns an optional `Int` value.

```swift
let data = ["a": "1", "b": "three", "c": "///4///"]

let m: [String: Int?] = data.mapValues { str in Int(str) }
// ["a": Optional(1), "b": nil, "c": nil]

let c: [String: Int] = data.compactMapValues { str in Int(str) }
// ["a": 1]
```

> **Note**: O( + ), where  is the length of the original dictionary and  is the length of the resulting dictionary.

## Parameters

- `transform`: A closure that transforms a value.    accepts each value of the dictionary as its parameter and returns an   optional transformed value of the same or of a different type.

## See Also

- [func mapValues<T>((Value) throws -> T) rethrows -> Dictionary<Key, T>](dictionary/mapvalues(_:).md)
  Returns a new dictionary containing the keys of this dictionary with the values transformed by the given closure.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](dictionary/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](dictionary/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dictionary/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](dictionary/flatmap(_:)-i3ly.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dictionary/flatmap(_:)-6chv9.md)
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](dictionary/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](dictionary/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](dictionary/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/compactmapvalues(_:))*