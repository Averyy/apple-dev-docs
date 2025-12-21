# floatsGroupRows

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the table view draws grouped rows as if they are floating.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var floatsGroupRows: Bool { get set }
```

#### Discussion

Group rows are rows for which the table view delegate’s [`tableView(_:isGroupRow:)`](nstableviewdelegate/tableview(_:isgrouprow:).md) method returns YES. These rows can be displayed as if they are floating in a view-based table view.

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/floatsgrouprows)*