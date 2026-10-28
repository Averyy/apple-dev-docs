# merge(partData:into:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method

Merges an individual part into the specified part of this object.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS

## Declaration

```swift
@discardableResult
mutating func merge(partData: MergeablePartData, into partID: AssignedWorkDocument.PartID) async throws -> Bool
```

## Return Value

`true`, if the merge caused a mutation.

## Parameters

- `partData`: The part data to merge into this object.
- `partID`: The part ID of the part that the incoming data should be merged in.

## See Also

### Merging the parts
- [func merge(AssignedWorkDocument) async throws -> Bool](./merge%28_%29.md)
  Merge another object of this type into this object.
- [func merge(other: AssignedWorkDocument) throws -> Bool](./merge%28other%29.md)
  Merge another object of this type into this object.
- [func merge(partID: AssignedWorkDocument.PartID, partDataURL: URL) throws -> Bool](./merge%28partid,partdataurl%29.md)
  Merges an individual part’s data into the specified part of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/merge(partdata:into:))*