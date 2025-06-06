# invalidationContextClass

**Framework**: AppKit  
**Kind**: property

Returns the class to use when creating an invalidation context object for the layout.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var invalidationContextClass: AnyClass { get }
```

#### Return Value

A custom class that descends from [`NSCollectionViewLayoutInvalidationContext`](nscollectionviewlayoutinvalidationcontext.md).

#### Discussion

If you define a custom invalidation context class to store information related to your layout, override this method and use it to return your custom subclass. Methods of this class that create invalidation contexts automatically create instances of the class you provide, initializing those instances using its [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) method.

## See Also

- [func invalidateLayout()](nscollectionviewlayout/invalidatelayout.md)
  Invalidates all layout information and triggers a layout update.
- [func invalidateLayout(with: NSCollectionViewLayoutInvalidationContext)](nscollectionviewlayout/invalidatelayout(with:).md)
  Invalidates specific parts of the layout using the specified context object.
- [func shouldInvalidateLayout(forBoundsChange: NSRect) -> Bool](nscollectionviewlayout/shouldinvalidatelayout(forboundschange:).md)
  Returns a Boolean indicating whether a bounds change triggers a layout update.
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> Bool](nscollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:).md)
  Returns a Boolean indicating whether changes to a cell’s layout attributes trigger a larger layout update.
- [func invalidationContext(forBoundsChange: NSRect) -> NSCollectionViewLayoutInvalidationContext](nscollectionviewlayout/invalidationcontext(forboundschange:).md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.
- [func invalidationContext(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutInvalidationContext](nscollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:).md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/invalidationcontextclass)*