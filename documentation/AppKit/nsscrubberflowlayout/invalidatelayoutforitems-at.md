# invalidateLayoutForItems(at:)

**Framework**: AppKit  
**Kind**: method

Informs the scrubber that it should perform a new layout pass for the items at the specified indexes.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func invalidateLayoutForItems(at invalidItemIndexes: IndexSet)
```

## Parameters

- `invalidItemIndexes`: An index set containing the indexes of the items whose layout should be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberflowlayout/invalidatelayoutforitems(at:))*