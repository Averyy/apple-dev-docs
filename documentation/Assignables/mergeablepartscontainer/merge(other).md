# merge(other:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Merge another object of this type into this object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

> **Deprecated**: Use merge(_:)

## Declaration

```swift
mutating func merge(other: Self) throws -> Bool
```

## Parameters

- `other`: The other object to merge into this one.

## See Also

### Merging the parts
- [func merge(partID: Self.PartID, partDataURL: URL) throws -> Bool](./merge%28partid,partdataurl%29.md)
  Merges an individual part into the specified part of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeablepartscontainer/merge(other:))*