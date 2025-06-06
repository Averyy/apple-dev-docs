# map(_:)

**Framework**: Swift  
**Kind**: method

Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.

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
func map<Transformed>(_ transform: @escaping (Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>
```

#### Return Value

An asynchronous sequence that contains, in order, the elements produced by the `transform` closure.

#### Discussion

Use the `map(_:)` method to transform every element received from a base asynchronous sequence. Typically, you use this to transform from one type of element to another.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `5`. The closure provided to the `map(_:)` method takes each `Int` and looks up a corresponding `String` from a `romanNumeralDict` dictionary. This means the outer `for await in` loop iterates over `String` instances instead of the underlying `Int` values that `Counter` produces:

```swift
let romanNumeralDict: [Int: String] =
    [1: "I", 2: "II", 3: "III", 5: "V"]

let stream = Counter(howHigh: 5)
    .map { romanNumeralDict[$0] ?? "(unknown)" }
for await numeral in stream {
    print(numeral, terminator: " ")
}
// Prints "I II III (unknown) V "
```

## Parameters

- `transform`: A mapping closure.   accepts an element   of this sequence as its parameter and returns a transformed value of the   same or of a different type.

## See Also

- [struct AsyncMapSequence](asyncmapsequence.md)
  An asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](asyncsequence/map(_:)-70wgb.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [struct AsyncThrowingMapSequence](asyncthrowingmapsequence.md)
  An asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](asyncsequence/compactmap(_:)-gfdq.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [struct AsyncCompactMapSequence](asynccompactmapsequence.md)
  An asynchronous sequence that maps a given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](asyncsequence/compactmap(_:)-1f8zn.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [struct AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md)
  An asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [struct AsyncFlatMapSequence](asyncflatmapsequence.md)
  An asynchronous sequence that concatenates the results of calling a given transformation with each element of this sequence.
- [struct AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md)
  An asynchronous sequence that concatenates the results of calling a given error-throwing transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](asyncsequence/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](asyncsequence/reduce(into:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/map(_:)-1q1k3)*