# enumerateAvailableRowViews(_:)

**Framework**: AppKit  
**Kind**: method

Allows the enumeration of all the table rows that are known to the table view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func enumerateAvailableRowViews(_ handler: (NSTableRowView, Int) -> Void)
```

#### Discussion

The enumeration includes all views in the [`visibleRect`](nsview/visiblerect.md); however, it may also include ones that are “in flight” due to animations or other attributes of the table.

It is preferred to use this method to efficiently make changes over all views that exist in the table.

> **Note**:  There is no guarantee that the rows will be enumerated in the displayed order.

## Parameters

- `handler`: The   takes two arguments:


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/enumerateavailablerowviews(_:))*