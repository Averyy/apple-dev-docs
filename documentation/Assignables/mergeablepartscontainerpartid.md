# MergeablePartsContainerPartID

**Framework**: Assignables  
**Kind**: struct

The ID of a part in a `MergeablePartsContainer`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct MergeablePartsContainerPartID
```

## Topics

### Initializers
- [init(String)](mergeablepartscontainerpartid/init(_:).md)
  Initiailizes an instance of a document part ID.
### Instance Properties
- [var rawValue: String](mergeablepartscontainerpartid/rawvalue.md)
  The underlying value of the part ID.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol MergeableDocument](mergeabledocument.md)
  Documents conforming to this protocol can merge several copies of the document into a single document.
- [protocol MergeableDocumentPage](mergeabledocumentpage.md)
  Types conforming to this protocol indicate that they are a page in a [`MergeableDocument`](mergeabledocument.md) conforming object.
- [protocol MergeablePartsContainer](mergeablepartscontainer.md)
  Objects conforming to this protocol allow merging in other replicas of themselves or merging in individual parts of themselves.
- [struct DocumentThumbnail](documentthumbnail.md)
  A structure that contains an image of an entire page or a portion of a page and the ID of the page the image is from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeablepartscontainerpartid)*