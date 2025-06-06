# compactMap(_:)

**Framework**: Swift  
**Kind**: method

Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.

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
func compactMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```

#### Return Value

An array of the non-`nil` results of calling `transform` with each element of the sequence.

#### Discussion

Use this method to receive an array of non-optional values when your transformation produces an optional value.

In this example, note the difference in the result of using `map` and `compactMap` with a transformation that returns an optional `Int` value.

```swift
let possibleNumbers = ["1", "2", "three", "///4///", "5"]

let mapped: [Int?] = possibleNumbers.map { str in Int(str) }
// [1, 2, nil, nil, 5]

let compactMapped: [Int] = possibleNumbers.compactMap { str in Int(str) }
// [1, 2, 5]
```

> **Note**: O(), where  is the length of this sequence.

O(), where  is the length of this sequence.

## Parameters

- `transform`: A closure that accepts an element of this   sequence as its argument and returns an optional value.

## See Also

- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](array/flatmap(_:)-i3mr.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](array/flatmap(_:)-6chu8.md)
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](array/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](array/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](array/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/compactmap(_:))*