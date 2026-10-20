# merge(other:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method

Merge another object of this type into this object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

> **Deprecated**: Use merge(_:)

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

### Merging the parts
- [func merge(AssignableDocument) async throws -> Bool](./merge%28_%29.md)
  Merge another object of this type into this object.
- [func merge(partData: MergeablePartData, into: AssignableDocument.PartID) async throws -> Bool](./merge%28partdata,into%29.md)
  Merges an individual part into the specified part of this object.
- [func merge(partID: AssignableDocument.PartID, partDataURL: URL) throws -> Bool](./merge%28partid,partdataurl%29.md)
  Merges an individual part’s data into the specified part of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/merge(other:))*