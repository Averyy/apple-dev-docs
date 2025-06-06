# replace(maxReplacements:content:with:)

**Framework**: Swift  
**Kind**: method

Replaces all matches for the regex in this collection, using the given closures to create the replacement and the regex.

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
mutating func replace<Output, Replacement>(maxReplacements: Int = .max, @RegexComponentBuilder content: () -> some RegexComponent, with replacement: (Regex<Output>.Match) throws -> Replacement) rethrows where Replacement : Collection, Replacement.Element == Character
```

## Parameters

- `maxReplacements`: A number specifying how many occurrences of   the regex to replace, using   to create the regex.
- `content`: A closure that returns the collection to search for   and replace.
- `replacement`: A closure that receives the full match information,   including captures, and returns a replacement collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/replace(maxreplacements:content:with:))*