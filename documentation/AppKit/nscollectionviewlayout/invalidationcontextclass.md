# invalidationContextClass

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the class to use when creating an invalidation context object for the layout.

**Availability**:
- macOS

## Declaration

```swift
class var invalidationContextClass: AnyClass { get }
```

```objc
@property (class, readonly) Class invalidationContextClass;
```

#### Return Value

A custom class that descends from [`NSCollectionViewLayoutInvalidationContext`](../nscollectionviewlayoutinvalidationcontext.md).

#### Discussion

If you define a custom invalidation context class to store information related to your layout, override this method and use it to return your custom subclass. Methods of this class that create invalidation contexts automatically create instances of the class you provide, initializing those instances using its [`init()`](../../ObjectiveC/nsobject-swift.class/init%28%29.md) method.

## See Also

### Invalidating the Layout
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Invalidates all layout information and triggers a layout update.
- [func invalidateLayout(with: NSCollectionViewLayoutInvalidationContext)](./invalidatelayout%28with%29.md)
  Invalidates specific parts of the layout using the specified context object.
- [func shouldInvalidateLayout(forBoundsChange: NSRect) -> Bool](./shouldinvalidatelayout%28forboundschange%29.md)
  Returns a Boolean indicating whether a bounds change triggers a layout update.
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> Bool](./shouldinvalidatelayout%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Returns a Boolean indicating whether changes to a cell’s layout attributes trigger a larger layout update.
- [func invalidationContext(forBoundsChange: NSRect) -> NSCollectionViewLayoutInvalidationContext](./invalidationcontext%28forboundschange%29.md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.
- [func invalidationContext(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutInvalidationContext](./invalidationcontext%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/invalidationcontextclass)*