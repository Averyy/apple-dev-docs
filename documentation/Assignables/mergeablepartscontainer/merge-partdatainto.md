# merge(partData:into:)

**Framework**: Assignables  
**Kind**: method  
**Required**: Yes

Merges an individual part into the specified part of this object.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS ?+

## Declaration

```swift
mutating func merge(partData: MergeablePartData, into partID: Self.PartID) async throws -> Bool
```

#### Return Value

`true`, if the merge caused a mutation.

## Parameters

- `partData`: The part data to merge into this object.
- `partID`: The part ID of the part that the incoming data should be merged in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeablepartscontainer/merge(partdata:into:))*