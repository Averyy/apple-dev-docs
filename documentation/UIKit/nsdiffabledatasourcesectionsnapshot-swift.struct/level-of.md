# level(of:)

**Framework**: UIKit  
**Kind**: method

Finds the hierarchical level of the specified item in the section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
func level(of item: ItemIdentifierType) -> Int
```

#### Discussion

A level of `0` means the item is at the root level of the section snapshot.

## See Also

- [func index(of: ItemIdentifierType) -> Int?](nsdiffabledatasourcesectionsnapshot-swift.struct/index(of:).md)
  Finds the index of the specified item in the section snapshot.
- [func parent(of: ItemIdentifierType) -> ItemIdentifierType?](nsdiffabledatasourcesectionsnapshot-swift.struct/parent(of:).md)
  Finds the parent item of the specified item in the section snapshot.
- [func contains(ItemIdentifierType) -> Bool](nsdiffabledatasourcesectionsnapshot-swift.struct/contains(_:).md)
  Indicates whether the section snapshot contains the specified item.
- [func isVisible(ItemIdentifierType) -> Bool](nsdiffabledatasourcesectionsnapshot-swift.struct/isvisible(_:).md)
  Indicates whether the specified item is currently visible onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/level(of:))*