# replacing(with:subrange:maxReplacements:content:)

**Framework**: Swift  
**Kind**: method

Returns a new collection in which all matches for the regex are replaced, using the given closure to create the regex.

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
func replacing<Replacement>(with replacement: Replacement, subrange: Range<Self.Index>, maxReplacements: Int = .max, @RegexComponentBuilder content: () -> some RegexComponent) -> Self where Replacement : Collection, Replacement.Element == Character
```

#### Return Value

A new collection in which all matches for regex in `subrange` are replaced by `replacement`, using `content` to create the regex.

## Parameters

- `replacement`: The new elements to add to the collection in place of   each match for the regex, using   to create the regex.
- `subrange`: The range in the collection in which to search for   the regex.
- `maxReplacements`: A number specifying how many occurrences of   the regex to replace.
- `content`: A closure that returns the collection to search for   and replace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/replacing(with:subrange:maxreplacements:content:))*