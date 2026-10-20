# contains(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether the section snapshot contains the specified item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
func contains(_ item: ItemIdentifierType) -> Bool
```

## See Also

### Getting item metrics
- [func index(of: ItemIdentifierType) -> Int?](./index%28of%29.md)
  Finds the index of the specified item in the section snapshot.
- [func level(of: ItemIdentifierType) -> Int](./level%28of%29.md)
  Finds the hierarchical level of the specified item in the section snapshot.
- [func parent(of: ItemIdentifierType) -> ItemIdentifierType?](./parent%28of%29.md)
  Finds the parent item of the specified item in the section snapshot.
- [func isVisible(ItemIdentifierType) -> Bool](./isvisible%28_%29.md)
  Indicates whether the specified item is currently visible onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/contains(_:))*