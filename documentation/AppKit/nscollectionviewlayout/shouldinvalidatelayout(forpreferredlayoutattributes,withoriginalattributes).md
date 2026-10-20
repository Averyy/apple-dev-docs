# shouldInvalidateLayout(forPreferredLayoutAttributes:withOriginalAttributes:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean indicating whether changes to a cell’s layout attributes trigger a larger layout update.

**Availability**:
- macOS

## Declaration

```swift
func shouldInvalidateLayout(forPreferredLayoutAttributes preferredAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: NSCollectionViewLayoutAttributes) -> Bool
```

```objc
- (BOOL) shouldInvalidateLayoutForPreferredLayoutAttributes:(NSCollectionViewLayoutAttributes *) preferredAttributes withOriginalAttributes:(NSCollectionViewLayoutAttributes *) originalAttributes;
```

#### Return Value

[`true`](../../Swift/true.md) if the layout should be invalidated or [`false`](../../Swift/false.md) if it should not.

#### Discussion

The default implementation of this method returns NO to indicate that layout is not needed. You can override this method in your custom layout classes and return a different value as needed. Your implementation of this method should determine if the new attributes would cause changes to the layout of other portions of the collection view.

If you return [`true`](../../Swift/true.md) from this method, the collection view invalidates the layout using the [`invalidateLayout(with:)`](./invalidatelayout%28with%29.md) method. The invalidation context passed to that method is created using the [`invalidationContext(forPreferredLayoutAttributes:withOriginalAttributes:)`](./invalidationcontext%28forpreferredlayoutattributes,withoriginalattributes%29.md) method.

## Parameters

- `preferredAttributes`: The preferred layout attributes of an element.
- `originalAttributes`: The attributes that the layout object originally suggested for the item.

## See Also

### Invalidating the Layout
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Invalidates all layout information and triggers a layout update.
- [func invalidateLayout(with: NSCollectionViewLayoutInvalidationContext)](./invalidatelayout%28with%29.md)
  Invalidates specific parts of the layout using the specified context object.
- [class var invalidationContextClass: AnyClass](./invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context object for the layout.
- [func shouldInvalidateLayout(forBoundsChange: NSRect) -> Bool](./shouldinvalidatelayout%28forboundschange%29.md)
  Returns a Boolean indicating whether a bounds change triggers a layout update.
- [func invalidationContext(forBoundsChange: NSRect) -> NSCollectionViewLayoutInvalidationContext](./invalidationcontext%28forboundschange%29.md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.
- [func invalidationContext(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutInvalidationContext](./invalidationcontext%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:))*