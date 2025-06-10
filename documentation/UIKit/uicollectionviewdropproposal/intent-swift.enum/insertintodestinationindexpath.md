# UICollectionViewDropProposal.Intent.insertIntoDestinationIndexPath

**Framework**: UIKit  
**Kind**: case

Incorporate the dropped items into the item at the specified index path.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case insertIntoDestinationIndexPath
```

#### Discussion

Use this option when the drop target has nested content. Dropping items with this proposal causes them to be added to the drop target’s children. For example, if the drop target is a folder, use this option to add the items to the contents of that folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropproposal/intent-swift.enum/insertintodestinationindexpath)*