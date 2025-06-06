# indices(where:)

**Framework**: RealityKit  
**Kind**: method

Returns the indices of all the elements that match the given predicate.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func indices(where predicate: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>
```

#### Return Value

A set of the indices of the elements for which `predicate` returns `true`.

#### Discussion

For example, you can use this method to find all the places that a vowel occurs in a string.

```None
let str = "Fresh cheese in a breeze"
let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
let allTheVowels = str.indices(where: { vowels.contains($0) })
// str[allTheVowels].count == 9
```

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element as its argument   and returns a Boolean value that indicates whether the passed element   represents a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewentitycollection/indices(where:))*