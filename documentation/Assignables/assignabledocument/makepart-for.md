# makePart(for:)

**Framework**: Assignables  
**Kind**: method

Creates data for the part with the given identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS ?+

## Declaration

```swift
func makePart(for partID: AssignableDocument.PartID) throws -> MergeablePartData?
```

#### Return Value

Part data for the `partID` provided, if possible. Otherwise, `nil`.

#### Discussion

In cases where this document is a partial one, i.e. it is missing some parts, you use this method to create data for the missing part. You then use [`merge(partData:into:)`](assignabledocument/merge(partdata:into:).md) to merge the newly created data into this document.

## Parameters

- `partID`: The identifier for the part you want to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/makepart(for:))*