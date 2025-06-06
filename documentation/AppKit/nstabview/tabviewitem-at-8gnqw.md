# tabViewItem(at:)

**Framework**: AppKit  
**Kind**: method

Returns the tab view item at the specified point.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func tabViewItem(at point: NSPoint) -> NSTabViewItem?
```

#### Return Value

The tab view item under the hit point, or `nil` if no tab view item is under that location.

#### Discussion

You can use this method to find a tab view item based on a user’s mouse click.

## Parameters

- `point`: The hit point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/tabviewitem(at:)-8gnqw)*