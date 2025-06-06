# replace(_:with:maxReplacements:)

**Framework**: Swift  
**Kind**: method

Replaces all occurrences of the sequence matching the given regex with a given collection.

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
mutating func replace<Replacement>(_ regex: some RegexComponent, with replacement: Replacement, maxReplacements: Int = .max) where Replacement : Collection, Replacement.Element == Character
```

## Parameters

- `regex`: A regex describing the sequence to replace.
- `replacement`: The new elements to add to the collection.
- `maxReplacements`: A number specifying how many occurrences of the   sequence matching   to replace. Default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/replace(_:with:maxreplacements:)-20ctz)*