# invalidateAttributes(in:)

**Framework**: UIKit  
**Kind**: method

Invalidates attributes in the specified range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func invalidateAttributes(in range: NSRange)
```

#### Discussion

Called from [`processEditing()`](nstextstorage/processediting().md) to invalidate attributes when the text storage changes. If the receiver isn’t lazy, this method calls [`fixAttributes(in:)`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1533823-fixattributes). If lazy attribute fixing is in effect, this method instead records the range needing fixing.

## Parameters

- `range`: The range of characters whose attributes the method should invalidate.

## See Also

- [func ensureAttributesAreFixed(in: NSRange)](nstextstorage/ensureattributesarefixed(in:).md)
  Ensures that attribute fixing occurs in the specified range.
- [var fixesAttributesLazily: Bool](nstextstorage/fixesattributeslazily.md)
  A Boolean value that indicates whether the text storage object fixes attributes lazily.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/invalidateattributes(in:))*