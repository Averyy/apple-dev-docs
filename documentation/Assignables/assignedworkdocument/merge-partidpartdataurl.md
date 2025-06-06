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
mutating func merge(partID: AssignedWorkDocument.PartID, partDataURL: URL) throws -> Bool
```

## Parameters

- `partID`: The part ID to merge in.
- `partDataURL`: The URL to the part data to merge in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/merge(partid:partdataurl:))*