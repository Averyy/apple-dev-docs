# itemViewForItem(at:)

**Framework**: AppKit  
**Kind**: method

Returns the view for the item at the specified index.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func itemViewForItem(at index: Int) -> NSScrubberItemView?
```

#### Return Value

The view for the specified index or `nil` if the item is not currently visible.

## Parameters

- `index`: The index of the item whose view you want.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/itemviewforitem(at:))*