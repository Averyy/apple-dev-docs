# level(of:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Finds the hierarchical level of the specified item in the section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
func level(of item: ItemIdentifierType) -> Int
```

#### Discussion

A level of `0` means the item is at the root level of the section snapshot.

## See Also

### Getting item metrics
- [func index(of: ItemIdentifierType) -> Int?](./index%28of%29.md)
  Finds the index of the specified item in the section snapshot.
- [func parent(of: ItemIdentifierType) -> ItemIdentifierType?](./parent%28of%29.md)
  Finds the parent item of the specified item in the section snapshot.
- [func contains(ItemIdentifierType) -> Bool](./contains%28_%29.md)
  Indicates whether the section snapshot contains the specified item.
- [func isVisible(ItemIdentifierType) -> Bool](./isvisible%28_%29.md)
  Indicates whether the specified item is currently visible onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/level(of:))*