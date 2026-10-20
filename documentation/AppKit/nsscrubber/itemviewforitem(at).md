# itemViewForItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the view for the item at the specified index.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func itemViewForItem(at index: Int) -> NSScrubberItemView?
```

```objc
- (NSScrubberItemView *) itemViewForItemAtIndex:(NSInteger) index;
```

#### Return Value

The view for the specified index or `nil` if the item is not currently visible.

## Parameters

- `index`: The index of the item whose view you want.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/itemviewforitem(at:))*