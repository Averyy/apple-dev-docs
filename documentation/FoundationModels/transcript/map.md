# map(_:)

**Framework**: Foundation Models  
**Kind**: method

Returns an array containing the results of mapping the given closure over the sequence’s elements.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func map<T, E>(_ transform: (Self.Element) throws(E) -> T) throws(E) -> [T] where E : Error
```

#### Return Value

An array containing the transformed elements of this sequence.

#### Discussion

In this example, `map` is used first to convert the names in the array to lowercase strings and then to count their characters.

```None
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let lowercaseNames = cast.map { $0.lowercased() }
// 'lowercaseNames' == ["vivien", "marlon", "kim", "karl"]
let letterCounts = cast.map { $0.count }
// 'letterCounts' == [6, 6, 3, 4]
```

> **Note**: O(), where  is the length of the sequence.

## Parameters

- `transform`: A mapping closure.   accepts an   element of this sequence as its parameter and returns a transformed   value of the same or of a different type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/map(_:))*