# ranges(of:)

**Framework**: Create ML Components  
**Kind**: method

Finds and returns the ranges of the all occurrences of a given sequence within the collection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func ranges<C>(of other: C) -> [Range<Self.Index>] where C : Collection, Self.Element == C.Element
```

#### Return Value

A collection of ranges of all occurrences of `other`. Returns an empty collection if `other` is not found.

## Parameters

- `other`: The sequence to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindows/ranges(of:))*