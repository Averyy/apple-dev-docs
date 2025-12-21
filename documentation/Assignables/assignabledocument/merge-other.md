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
mutating func merge(other: AssignableDocument) throws -> Bool
```

#### Discussion

An exception is thrown if `other` is not a replica of this document.

## Parameters

- `other`: The other object to merge into this one.

## See Also

- [func merge(AssignableDocument) async throws -> Bool](assignabledocument/merge(_:).md)
  Merge another object of this type into this object.
- [func merge(partData: MergeablePartData, into: AssignableDocument.PartID) async throws -> Bool](assignabledocument/merge(partdata:into:).md)
  Merges an individual part into the specified part of this object.
- [func merge(partID: AssignableDocument.PartID, partDataURL: URL) throws -> Bool](assignabledocument/merge(partid:partdataurl:).md)
  Merges an individual part’s data into the specified part of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/merge(other:))*