# invalidationContext(forPreferredLayoutAttributes:withOriginalAttributes:)

**Framework**: AppKit  
**Kind**: method

Returns an invalidation context object that defines the portions of the layout that need to be updated.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func invalidationContext(forPreferredLayoutAttributes preferredAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutInvalidationContext
```

#### Return Value

An invalidation context that describes the changes to be made. This value is never `nil`.

#### Discussion

The default implementation of this method creates an instance of the class returned by the [`invalidationContextClass`](nscollectionviewlayout/invalidationcontextclass.md) method and initializes it using its [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) method. Subclasses can override this method and configure additional properties of the invalidation context. In your implementation, you must call `super` first to get the context object; you can then configure that object and return it.

## Parameters

- `preferredAttributes`: The preferred layout attributes of an element.
- `originalAttributes`: The attributes that the layout object originally suggested for the item.

## See Also

- [func invalidateLayout()](nscollectionviewlayout/invalidatelayout.md)
  Invalidates all layout information and triggers a layout update.
- [func invalidateLayout(with: NSCollectionViewLayoutInvalidationContext)](nscollectionviewlayout/invalidatelayout(with:).md)
  Invalidates specific parts of the layout using the specified context object.
- [class var invalidationContextClass: AnyClass](nscollectionviewlayout/invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context object for the layout.
- [func shouldInvalidateLayout(forBoundsChange: NSRect) -> Bool](nscollectionviewlayout/shouldinvalidatelayout(forboundschange:).md)
  Returns a Boolean indicating whether a bounds change triggers a layout update.
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> Bool](nscollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:).md)
  Returns a Boolean indicating whether changes to a cell’s layout attributes trigger a larger layout update.
- [func invalidationContext(forBoundsChange: NSRect) -> NSCollectionViewLayoutInvalidationContext](nscollectionviewlayout/invalidationcontext(forboundschange:).md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:))*