# invalidateLayout()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invalidates all layout information and triggers a layout update.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func invalidateLayout()
```

```objc
- (void) invalidateLayout;
```

#### Discussion

Call this method when you make changes that require updating all of the current layout information. This method marks the layout as invalid and returns right away, so you can call this method multiple times from the same block of code without triggering multiple layout updates. During the next update cycle, the collection view requests new layout information and updates its contents accordingly.

If you override this method, you must call `super` at some point in your implementation.

## See Also

### Invalidating the Layout
- [func invalidateLayout(with: NSCollectionViewLayoutInvalidationContext)](./invalidatelayout%28with%29.md)
  Invalidates specific parts of the layout using the specified context object.
- [class var invalidationContextClass: AnyClass](./invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context object for the layout.
- [func shouldInvalidateLayout(forBoundsChange: NSRect) -> Bool](./shouldinvalidatelayout%28forboundschange%29.md)
  Returns a Boolean indicating whether a bounds change triggers a layout update.
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> Bool](./shouldinvalidatelayout%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Returns a Boolean indicating whether changes to a cell’s layout attributes trigger a larger layout update.
- [func invalidationContext(forBoundsChange: NSRect) -> NSCollectionViewLayoutInvalidationContext](./invalidationcontext%28forboundschange%29.md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.
- [func invalidationContext(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutInvalidationContext](./invalidationcontext%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/invalidatelayout())*