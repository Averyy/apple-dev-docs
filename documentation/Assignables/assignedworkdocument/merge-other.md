# merge(other:)

**Framework**: Assignables  
**Kind**: method

Merge another object of this type into this object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
@discardableResult
mutating func merge(other: AssignedWorkDocument) throws -> Bool
```

## Parameters

- `other`: The other object to merge into this one.

## See Also

- [func merge(AssignedWorkDocument) async throws -> Bool](assignedworkdocument/merge(_:).md)
  Merge another object of this type into this object.
- [func merge(partData: MergeablePartData, into: AssignedWorkDocument.PartID) async throws -> Bool](assignedworkdocument/merge(partdata:into:).md)
  Merges an individual part into the specified part of this object.
- [func merge(partID: AssignedWorkDocument.PartID, partDataURL: URL) throws -> Bool](assignedworkdocument/merge(partid:partdataurl:).md)
  Merges an individual part’s data into the specified part of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/merge(other:))*