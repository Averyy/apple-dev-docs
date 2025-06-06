# replacing(_:with:maxReplacements:)

**Framework**: MusicKit  
**Kind**: method

Returns a new collection in which all occurrences of a target sequence are replaced by another collection.

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
func replacing<C, Replacement>(_ other: C, with replacement: Replacement, maxReplacements: Int = .max) -> Self where C : Collection, Replacement : Collection, Self.Element == C.Element, C.Element == Replacement.Element
```

#### Return Value

A new collection in which all occurrences of `other` in `subrange` of the collection are replaced by `replacement`.

## Parameters

- `other`: The sequence to replace.
- `replacement`: The new elements to add to the collection.
- `maxReplacements`: A number specifying how many occurrences of    to replace. Default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/replacing(_:with:maxreplacements:))*