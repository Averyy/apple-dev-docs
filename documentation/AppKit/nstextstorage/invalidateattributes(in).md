# invalidateAttributes(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invalidates attributes in the specified range.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func invalidateAttributes(in range: NSRange)
```

```objc
- (void) invalidateAttributesInRange:(NSRange) range;
```

#### Discussion

Called from [`processEditing()`](./processediting%28%29.md) to invalidate attributes when the text storage changes. If the receiver isn’t lazy, this method calls [`fixAttributes(in:)`](../../Foundation/nsmutableattributedstring/fixattributes%28in%29.md). If lazy attribute fixing is in effect, this method instead records the range needing fixing.

## Parameters

- `range`: The range of characters whose attributes the method should invalidate.

## See Also

### Fixing the string attributes
- [func ensureAttributesAreFixed(in: NSRange)](./ensureattributesarefixed%28in%29.md)
  Ensures that attribute fixing occurs in the specified range.
- [var fixesAttributesLazily: Bool](./fixesattributeslazily.md)
  A Boolean value that indicates whether the text storage object fixes attributes lazily.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/invalidateattributes(in:))*