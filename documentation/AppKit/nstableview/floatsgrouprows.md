# floatsGroupRows

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the table view draws grouped rows as if they are floating.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var floatsGroupRows: Bool { get set }
```

```objc
@property BOOL floatsGroupRows;
```

#### Discussion

Group rows are rows for which the table view delegate’s [`tableView(_:isGroupRow:)`](../nstableviewdelegate/tableview%28_,isgrouprow%29.md) method returns YES. These rows can be displayed as if they are floating in a view-based table view.

The default value of this property is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/floatsgrouprows)*