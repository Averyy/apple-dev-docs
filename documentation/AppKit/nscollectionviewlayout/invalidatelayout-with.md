# invalidateLayout(with:)

**Framework**: AppKit  
**Kind**: method

Invalidates specific parts of the layout using the specified context object.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func invalidateLayout(with context: NSCollectionViewLayoutInvalidationContext)
```

#### Discussion

Call this method when you make changes that need to be reflected by the collection view, but which do not require the replacement of all of the layout information. You use this method to minimize the work performed by the layout object. Instead of optimizing everything, the specified context object indicates which parts of the layout need to be recomputed. All other layout information is left alone.

When implementing a custom layout, you can override this method and use it to process information provided by a custom invalidation context. You are not required to provide a custom invalidation context but might do so if you are able to provide additional properties that can help optimize layout updates. If you override this method, you must call `super` at some point in your implementation.

## Parameters

- `context`: The context object indicating which parts of the layout need to be updated.

## See Also

- [func invalidateLayout()](nscollectionviewlayout/invalidatelayout.md)
  Invalidates all layout information and triggers a layout update.
- [class var invalidationContextClass: AnyClass](nscollectionviewlayout/invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context object for the layout.
- [func shouldInvalidateLayout(forBoundsChange: NSRect) -> Bool](nscollectionviewlayout/shouldinvalidatelayout(forboundschange:).md)
  Returns a Boolean indicating whether a bounds change triggers a layout update.
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> Bool](nscollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:).md)
  Returns a Boolean indicating whether changes to a cell’s layout attributes trigger a larger layout update.
- [func invalidationContext(forBoundsChange: NSRect) -> NSCollectionViewLayoutInvalidationContext](nscollectionviewlayout/invalidationcontext(forboundschange:).md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.
- [func invalidationContext(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutInvalidationContext](nscollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:).md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/invalidatelayout(with:))*