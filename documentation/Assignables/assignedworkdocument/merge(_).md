# merge(_:)

**Framework**: Assignables  
**Kind**: method

Merge another object of this type into this object.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS ?+

## Declaration

```swift
@discardableResult
mutating func merge(_ other: AssignedWorkDocument) async throws -> Bool
```

#### Return Value

`true`, if the merge caused a mutation.

## Parameters

- `other`: The other object to merge into this one.

## See Also

- [func merge(partData: MergeablePartData, into: AssignedWorkDocument.PartID) async throws -> Bool](assignedworkdocument/merge(partdata:into:).md)
  Merges an individual part into the specified part of this object.
- [func merge(other: AssignedWorkDocument) throws -> Bool](assignedworkdocument/merge(other:).md)
  Merge another object of this type into this object.
- [func merge(partID: AssignedWorkDocument.PartID, partDataURL: URL) throws -> Bool](assignedworkdocument/merge(partid:partdataurl:).md)
  Merges an individual part’s data into the specified part of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/merge(_:))*