# collectionViewLayout

**Framework**: AppKit  
**Kind**: property

The layout object used to organize the collection view’s content.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var collectionViewLayout: NSCollectionViewLayout? { get set }
```

#### Discussion

Typically, you specify the layout object at design time in Interface Builder. The layout object works with your data source object to generate the needed items and views to display. In macOS 10.11 and later, using a data source object is recommended, but you may specify `nil` for this property if your collection view does not use a data source object. The collection view uses the [`NSCollectionViewGridLayout`](nscollectionviewgridlayout.md) object by default.

Assigning a new value to this property changes the layout object and causes the collection view to update its contents immediately and without animations. If you want to animate a layout change, use an animator object to set the layout object as follows:

```objc
[[collectionView animator] setCollectionViewLayout:myLayout];
```

You can use the completion handler of the associated [`NSAnimationContext`](nsanimationcontext.md) object to perform additional tasks when the animations finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/collectionviewlayout)*