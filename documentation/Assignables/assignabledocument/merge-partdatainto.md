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
mutating func merge(partData: MergeablePartData, into partID: AssignableDocument.PartID) async throws -> Bool
```

#### Return Value

`true`, if the merge caused a mutation.

## Parameters

- `partData`: The part data to merge into this object.
- `partID`: The part ID of the part that the incoming data should be merged in.

## See Also

- [func merge(AssignableDocument) async throws -> Bool](assignabledocument/merge(_:).md)
  Merge another object of this type into this object.
- [func merge(other: AssignableDocument) throws -> Bool](assignabledocument/merge(other:).md)
  Merge another object of this type into this object.
- [func merge(partID: AssignableDocument.PartID, partDataURL: URL) throws -> Bool](assignabledocument/merge(partid:partdataurl:).md)
  Merges an individual part’s data into the specified part of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/merge(partdata:into:))*