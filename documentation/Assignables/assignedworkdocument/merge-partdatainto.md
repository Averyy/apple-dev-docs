# merge(partData:into:)

**Framework**: Assignables  
**Kind**: method

Merges an individual part into the specified part of this object.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS ?+

## Declaration

```swift
@discardableResult
mutating func merge(partData: MergeablePartData, into partID: AssignedWorkDocument.PartID) async throws -> Bool
```

#### Return Value

`true`, if the merge caused a mutation.

## Parameters

- `partData`: The part data to merge into this object.
- `partID`: The part ID of the part that the incoming data should be merged in.

## See Also

- [func merge(AssignedWorkDocument) async throws -> Bool](assignedworkdocument/merge(_:).md)
  Merge another object of this type into this object.
- [func merge(other: AssignedWorkDocument) throws -> Bool](assignedworkdocument/merge(other:).md)
  Merge another object of this type into this object.
- [func merge(partID: AssignedWorkDocument.PartID, partDataURL: URL) throws -> Bool](assignedworkdocument/merge(partid:partdataurl:).md)
  Merges an individual part’s data into the specified part of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/merge(partdata:into:))*