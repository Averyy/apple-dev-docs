# shouldInvalidateLayout(forPreferredLayoutAttributes:withOriginalAttributes:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean indicating whether changes to a cell’s layout attributes trigger a larger layout update.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func shouldInvalidateLayout(forPreferredLayoutAttributes preferredAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: NSCollectionViewLayoutAttributes) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the layout should be invalidated or [`false`](https://developer.apple.com/documentation/Swift/false) if it should not.

#### Discussion

The default implementation of this method returns NO to indicate that layout is not needed. You can override this method in your custom layout classes and return a different value as needed. Your implementation of this method should determine if the new attributes would cause changes to the layout of other portions of the collection view.

If you return [`true`](https://developer.apple.com/documentation/Swift/true) from this method, the collection view invalidates the layout using the [`invalidateLayout(with:)`](nscollectionviewlayout/invalidatelayout(with:).md) method. The invalidation context passed to that method is created using the [`invalidationContext(forPreferredLayoutAttributes:withOriginalAttributes:)`](nscollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:).md) method.

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
- [func invalidationContext(forBoundsChange: NSRect) -> NSCollectionViewLayoutInvalidationContext](nscollectionviewlayout/invalidationcontext(forboundschange:).md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.
- [func invalidationContext(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutInvalidationContext](nscollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:).md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:))*