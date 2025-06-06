# replacing(_:subrange:maxReplacements:with:)

**Framework**: Swift  
**Kind**: method

Returns a new collection in which all occurrences of a sequence matching the given regex are replaced by another regex match.

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
func replacing<Output, Replacement>(_ regex: some RegexComponent, subrange: Range<Self.Index>, maxReplacements: Int = .max, with replacement: (Regex<Output>.Match) throws -> Replacement) rethrows -> Self where Replacement : Collection, Replacement.Element == Character
```

#### Return Value

A new collection in which all occurrences of subsequence matching `regex` are replaced by `replacement`.

## Parameters

- `regex`: A regex describing the sequence to replace.
- `subrange`: The range in the collection in which to search for  .
- `maxReplacements`: A number specifying how many occurrences of the   sequence matching   to replace. Default is  .
- `replacement`: A closure that receives the full match information,   including captures, and returns a replacement collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/replacing(_:subrange:maxreplacements:with:))*