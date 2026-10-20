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
- visionOS 1.0+

## Declaration

```swift
func isExpanded(_ item: Any) -> Bool
```

```objc
- (BOOL) isExpanded:(ItemIdentifierType) item;
```

#### Discussion

This expansion state persists along with the section snapshot.

## See Also

### Expanding and collapsing items
- [func expandItems([Any])](./expanditems%28_%29.md)
  Expands the specified items in the section snapshot.
- [func collapseItems([Any])](./collapseitems%28_%29.md)
  Collapses the specified items in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/isexpanded(_:))*