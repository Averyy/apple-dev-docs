# replacing(_:with:subrange:maxReplacements:)

**Framework**: Swift  
**Kind**: method

Returns a new collection in which all occurrences of a sequence matching the given regex are replaced by another collection.

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
func replacing<Replacement>(_ regex: some RegexComponent, with replacement: Replacement, subrange: Range<Self.Index>, maxReplacements: Int = .max) -> Self where Replacement : Collection, Replacement.Element == Character
```

#### Return Value

A new collection in which all occurrences of subsequence matching `regex` in `subrange` are replaced by `replacement`.

## Parameters

- `regex`: A regex describing the sequence to replace.
- `replacement`: The new elements to add to the collection.
- `subrange`: The range in the collection in which to search for  .
- `maxReplacements`: A number specifying how many occurrences of the   sequence matching   to replace. Default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/replacing(_:with:subrange:maxreplacements:)-5mdsz)*