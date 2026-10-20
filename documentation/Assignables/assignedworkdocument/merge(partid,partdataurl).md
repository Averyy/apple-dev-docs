# merge(partID:partDataURL:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method

Merges an individual part’s data into the specified part of this object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

> **Deprecated**: Use merge(partData:into:)

## Declaration

```swift
@discardableResult
mutating func merge(partID: AssignedWorkDocument.PartID, partDataURL: URL) throws -> Bool
```

## Parameters

- `partID`: The part ID to merge in.
- `partDataURL`: The URL to the part data to merge in.

## See Also

### Merging the parts
- [func merge(AssignedWorkDocument) async throws -> Bool](./merge%28_%29.md)
  Merge another object of this type into this object.
- [func merge(partData: MergeablePartData, into: AssignedWorkDocument.PartID) async throws -> Bool](./merge%28partdata,into%29.md)
  Merges an individual part into the specified part of this object.
- [func merge(other: AssignedWorkDocument) throws -> Bool](./merge%28other%29.md)
  Merge another object of this type into this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/merge(partid:partdataurl:))*