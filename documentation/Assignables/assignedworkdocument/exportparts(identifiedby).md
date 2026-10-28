# exportParts(identifiedBy:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method

Given a set of part identifiers, return a dictionary of part ID to part data.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS

## Declaration

```swift
func exportParts(identifiedBy partIDs: [AssignedWorkDocument.PartID]) async throws -> [AssignedWorkDocument.PartID : MergeablePartData]
```

## Return Value

A dictionary of part ID to part data file for the requested parts.

## Parameters

- `partIDs`: An array of part IDs to export. This is treated as a set.

## See Also

### Exporting the parts
- [func export(partIDs: [AssignedWorkDocument.PartID]) async throws -> [AssignedWorkDocument.PartID : URL]](./export%28partids%29.md)
  Given a set of part identifiers, return a dictionary of part ID to data objects for the requested parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/exportparts(identifiedby:))*