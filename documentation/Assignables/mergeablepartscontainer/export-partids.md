# export(partIDs:)

**Framework**: Assignables  
**Kind**: method  
**Required**: Yes

Given a set of part identifiers, return a dictionary of part ID to URL to the part data file for the requested parts.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- visionOS ?+
- Unknown ?+ - Deprecated
- Mac Catalyst 17.4+

## Declaration

```swift
func export(partIDs: [Self.PartID]) async throws -> [Self.PartID : URL]
```

#### Return Value

A dictionary of part ID to URL to the part data file for the requested parts.

## Parameters

- `partIDs`: An array of part IDs to export. This is treated as a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeablepartscontainer/export(partids:))*