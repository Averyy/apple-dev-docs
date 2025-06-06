# register(_:forDecorationViewOfKind:)

**Framework**: AppKit  
**Kind**: method

Registers a class to use when creating the layout’s decoration views.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func register(_ viewClass: AnyClass?, forDecorationViewOfKind elementKind: NSCollectionView.DecorationElementKind)
```

#### Discussion

Call this method as part of your layout object’s initialization and use it to register any decoration views needed for your layout. Decoration views are visual adornments that you include in your layouts and use to present the collection view’s content. For example, you might use decoration views to implement a dynamic background that can expand or shrink to match the current number of items. The layout object defines and owns the decoration views it uses. Decoration views do not have any ties to the collection view’s data source object.

After registering your decoration views, you create decoration views by returning an appropriate set of layout attributes from the [`layoutAttributesForElements(in:)`](nscollectionviewlayout/layoutattributesforelements(in:).md) method. When you return a [`NSCollectionViewLayoutAttributes`](nscollectionviewlayoutattributes.md) object configured for a decoration view, the collection view uses your registered nib or class information to create the corresponding views.

## Parameters

- `viewClass`: The class to use for the decoration view. This class must conform to the   protocol. Specify   to unregister a previously registered class or nib file.
- `elementKind`: The string your layout uses to identify the decoration view’s type. This parameter must not be   and must not be an empty string.

## See Also

- [func register(NSNib?, forDecorationViewOfKind: NSCollectionView.DecorationElementKind)](nscollectionviewlayout/register(_:fordecorationviewofkind:)-7z7uf.md)
  Registers a nib file to use when creating the layout’s decoration views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/register(_:fordecorationviewofkind:)-44qmc)*