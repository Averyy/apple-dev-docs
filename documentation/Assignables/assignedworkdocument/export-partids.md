# export(partIDs:)

**Framework**: Assignables  
**Kind**: method

Given a set of part identifiers, return a dictionary of part ID to data objects for the requested parts.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
func export(partIDs: [AssignedWorkDocument.PartID]) async throws -> [AssignedWorkDocument.PartID : URL]
```

#### Return Value

A dictionary of part ID to URLs of the data for the requested parts.

## Parameters

- `partIDs`: An array of part IDs to export. This is treated as a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/export(partids:))*