# merge(partID:partDataURL:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Merges an individual part into the specified part of this object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

> **Deprecated**: Use merge(partData:into:)

## Declaration

```swift
mutating func merge(partID: Self.PartID, partDataURL: URL) throws -> Bool
```

## Parameters

- `partID`: The part ID to merge in.
- `partDataURL`: The URL to the part data file to merge in.

## See Also

### Merging the parts
- [func merge(other: Self) throws -> Bool](./merge%28other%29.md)
  Merge another object of this type into this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeablepartscontainer/merge(partid:partdataurl:))*