# isHidden

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the table column is hidden.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var isHidden: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the table column is hidden. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

Columns that are hidden still exist in the table view object’s [`tableColumns`](nstableview/tablecolumns.md) array and are included in the table view’s [`numberOfColumns`](nstableview/numberofcolumns.md) count.

The hidden state is stored when the table view autosaves the table column state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/ishidden)*