# invalidationContext(forBoundsChange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an invalidation context object that defines the portions of the layout that need to be updated.

**Availability**:
- macOS

## Declaration

```swift
func invalidationContext(forBoundsChange newBounds: NSRect) -> NSCollectionViewLayoutInvalidationContext
```

```objc
- (NSCollectionViewLayoutInvalidationContext *) invalidationContextForBoundsChange:(NSRect) newBounds;
```

#### Return Value

An invalidation context that describes the changes to be made. This value is never `nil`.

#### Discussion

The default implementation of this method creates an instance of the class returned by the [`invalidationContextClass`](./invalidationcontextclass.md) method and initializes it using its [`init()`](../../ObjectiveC/nsobject-swift.class/init%28%29.md) method. Subclasses can override this method and configure additional properties of the invalidation context. In your implementation, you must call `super` first to get the context object; you can then configure that object and return it.

## Parameters

- `newBounds`: The new bounds for the collection view.

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
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> Bool](./shouldinvalidatelayout%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Returns a Boolean indicating whether changes to a cell’s layout attributes trigger a larger layout update.
- [func invalidationContext(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutInvalidationContext](./invalidationcontext%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/invalidationcontext(forboundschange:))*