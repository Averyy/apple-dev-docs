# frameOfOutlineCell(atRow:)

**Framework**: AppKit  
**Kind**: method

Returns the frame of the outline cell for a given row.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func frameOfOutlineCell(atRow row: Int) -> NSRect
```

#### Return Value

The frame of the outline cell for the row at index `row`, considering the current indentation and the value in the [`indentationMarkerFollowsCell`](nsoutlineview/indentationmarkerfollowscell.md) property. If the row at index `row` is not an expandable row, returns `NSZeroRect`.

#### Discussion

You can override this method in a subclass to return a custom frame for the outline button cell. If your override returns an empty rect, no outline cell is drawn for that row. You might do that, for example, so that the disclosure triangle will not be shown for a row that should never be expanded.

## Parameters

- `row`: The index of the row for which to return the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/frameofoutlinecell(atrow:))*