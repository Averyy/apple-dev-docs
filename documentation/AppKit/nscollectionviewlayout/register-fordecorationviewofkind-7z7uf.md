# register(_:forDecorationViewOfKind:)

**Framework**: AppKit  
**Kind**: method

Registers a nib file to use when creating the layout’s decoration views.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func register(_ nib: NSNib?, forDecorationViewOfKind elementKind: NSCollectionView.DecorationElementKind)
```

#### Discussion

Call this method as part of your layout object’s initialization and use it to register any decoration views needed for your layout. Decoration views are visual adornments that you include in your layouts and use to present the collection view’s content. For example, you might use decoration views to implement a dynamic background that can expand or shrink to match the current number of items. The layout object defines and owns the decoration views it uses. Decoration views do not have any ties to the collection view’s data source object.

After registering your decoration views, you create decoration views by returning an appropriate set of layout attributes from the [`layoutAttributesForElements(in:)`](nscollectionviewlayout/layoutattributesforelements(in:).md) method. When you return a [`NSCollectionViewLayoutAttributes`](nscollectionviewlayoutattributes.md) object configured for a decoration view, the collection view uses your registered nib or class information to create the corresponding views.

## Parameters

- `nib`: The nib object containing the decoration view’s definition. The nib file must contain exactly one   object at the top level and that view must conform to the   protocol. Specify   to unregister a previously registered class or nib file.
- `elementKind`: The string your layout uses to identify the decoration view’s type. This parameter must not be   and must not be an empty string.

## See Also

- [func register(AnyClass?, forDecorationViewOfKind: NSCollectionView.DecorationElementKind)](nscollectionviewlayout/register(_:fordecorationviewofkind:)-44qmc.md)
  Registers a class to use when creating the layout’s decoration views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/register(_:fordecorationviewofkind:)-7z7uf)*