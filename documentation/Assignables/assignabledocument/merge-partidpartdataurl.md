# merge(partID:partDataURL:)

**Framework**: Assignables  
**Kind**: method

Merges an individual part’s data into the specified part of this object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- visionOS ?+
- Unknown ?+ - Deprecated
- Mac Catalyst 17.4+

## Declaration

```swift
@discardableResult
mutating func merge(partID: AssignableDocument.PartID, partDataURL: URL) throws -> Bool
```

## Parameters

- `partID`: The part ID to merge in.
- `partDataURL`: The URL to the part data to merge in.

## See Also

- [func merge(AssignableDocument) async throws -> Bool](assignabledocument/merge(_:).md)
  Merge another object of this type into this object.
- [func merge(partData: MergeablePartData, into: AssignableDocument.PartID) async throws -> Bool](assignabledocument/merge(partdata:into:).md)
  Merges an individual part into the specified part of this object.
- [func merge(other: AssignableDocument) throws -> Bool](assignabledocument/merge(other:).md)
  Merge another object of this type into this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/merge(partid:partdataurl:))*