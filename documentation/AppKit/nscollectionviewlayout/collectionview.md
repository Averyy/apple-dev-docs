# collectionView

**Framework**: AppKit  
**Kind**: property

The collection view object currently using this layout.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
weak var collectionView: NSCollectionView? { get }
```

#### Discussion

When you assign a layout object to a collection view, the collection view automatically updates this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/collectionview)*