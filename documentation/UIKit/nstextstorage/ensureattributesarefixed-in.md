# ensureAttributesAreFixed(in:)

**Framework**: UIKit  
**Kind**: method

Ensures that attribute fixing occurs in the specified range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func ensureAttributesAreFixed(in range: NSRange)
```

#### Discussion

An `NSTextStorage` object using lazy attribute fixing is required to call this method before accessing any attributes within `range`. This method gives attribute fixing a chance to occur if necessary. `NSTextStorage` subclasses wishing to support laziness must call this method from all attribute accessors they implement.

## Parameters

- `range`: The range of characters to examine.

## See Also

- [func invalidateAttributes(in: NSRange)](nstextstorage/invalidateattributes(in:).md)
  Invalidates attributes in the specified range.
- [var fixesAttributesLazily: Bool](nstextstorage/fixesattributeslazily.md)
  A Boolean value that indicates whether the text storage object fixes attributes lazily.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/ensureattributesarefixed(in:))*