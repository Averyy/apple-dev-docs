# init(operation:intent:)

**Framework**: UIKit  
**Kind**: init

Creates a drop proposal object that specifies how to incorporate the dropped content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(operation: UIDropOperation, intent: UICollectionViewDropProposal.Intent)
```

#### Return Value

An initialized drop proposal.

## Parameters

- `operation`: The type of operation that you want to perform. Use this parameter to specify whether you want to move the original item to this new location, move a copy of the content, or prevent the content from being inserted at this location. For a list of possible values, see  .
- `intent`: The option for how to incorporate the content into the collection view. You can insert the content between items or add it to an existing item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropproposal/init(operation:intent:))*