# sorted(using:)

**Framework**: Create ML  
**Kind**: method

Returns the elements of the sequence, sorted using the given comparator to compare elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func sorted<Comparator>(using comparator: Comparator) -> [Self.Element] where Comparator : SortComparator, Self.Element == Comparator.Compared
```

#### Return Value

An array of the elements sorted using `comparator`.

## Parameters

- `comparator`: The comparator to use in ordering elements


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/sorted(using:)-2frjp)*