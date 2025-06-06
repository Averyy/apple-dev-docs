# replace(_:with:maxReplacements:)

**Framework**: System  
**Kind**: method

Replaces all occurrences of a target sequence with a given collection

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
mutating func replace<C, Replacement>(_ other: C, with replacement: Replacement, maxReplacements: Int = .max) where C : Collection, Replacement : Collection, Self.Element == C.Element, C.Element == Replacement.Element
```

## Parameters

- `other`: The sequence to replace.
- `replacement`: The new elements to add to the collection.
- `maxReplacements`: A number specifying how many occurrences of    to replace. Default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/replace(_:with:maxreplacements:))*