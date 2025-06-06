# ensureAttributesAreFixed(in:)

**Framework**: AppKit  
**Kind**: method

Ensures that attribute fixing occurs in the specified range.

**Availability**:
- macOS 10.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/ensureattributesarefixed(in:))*