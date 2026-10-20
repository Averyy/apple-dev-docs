# isExpanded(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether the item with the specified identifier is in an expanded state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
func isExpanded(_ item: ItemIdentifierType) -> Bool
```

#### Discussion

This expansion state persists along with the section snapshot.

## See Also

### Expanding and collapsing items
- [func expand([ItemIdentifierType])](./expand%28_%29.md)
  Expands the specified items in the section snapshot.
- [func collapse([ItemIdentifierType])](./collapse%28_%29.md)
  Collapses the specified items in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/isexpanded(_:))*