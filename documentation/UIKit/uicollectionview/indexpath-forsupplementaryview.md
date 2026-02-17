# indexPath(forSupplementaryView:)

**Framework**: UIKit  
**Kind**: method

Gets the index path of the specified supplementary view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func indexPath(forSupplementaryView supplementaryView: UICollectionReusableView) -> IndexPath?
```

#### Return Value

The index path of the specified view if it is in the collection view, else `nil`.

## Parameters

- `supplementaryView`: The supplementary or decoration view whose index path you want.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/indexpath(forsupplementaryview:))*