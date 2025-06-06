# proposal

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The current proposal for how to incorporate the dropped items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var proposal: UICollectionViewDropProposal { get }
```

#### Discussion

If your drag delegate implements the [`collectionView(_:dropSessionDidUpdate:withDestinationIndexPath:)`](uicollectionviewdropdelegate/collectionview(_:dropsessiondidupdate:withdestinationindexpath:).md) method, this object contains the information that you provided when making your drop proposal for the given location.

## See Also

- [var session: any UIDropSession](uicollectionviewdropcoordinator/session.md)
  The drop session containing information about the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/proposal)*