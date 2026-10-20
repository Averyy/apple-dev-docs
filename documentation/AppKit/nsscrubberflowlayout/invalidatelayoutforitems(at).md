# invalidateLayoutForItems(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the scrubber that it should perform a new layout pass for the items at the specified indexes.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func invalidateLayoutForItems(at invalidItemIndexes: IndexSet)
```

```objc
- (void) invalidateLayoutForItemsAtIndexes:(NSIndexSet *) invalidItemIndexes;
```

## Parameters

- `invalidItemIndexes`: An index set containing the indexes of the items whose layout should be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberflowlayout/invalidatelayoutforitems(at:))*