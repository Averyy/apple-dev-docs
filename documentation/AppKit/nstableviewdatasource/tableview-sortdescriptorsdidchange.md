# tableView(_:sortDescriptorsDidChange:)

**Framework**: AppKit  
**Kind**: method

Called by `aTableView` to indicate that sorting may need to be done.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, sortDescriptorsDidChange oldDescriptors: [NSSortDescriptor])
```

#### Discussion

The data source typically sorts and reloads the data, and adjusts the selections accordingly. If you need to know the current sort descriptors and the data source doesn’t manage them itself, you can get the current sort descriptors by sending `aTableView` a [`sortDescriptors`](nstableview/sortdescriptors.md) message.

## Parameters

- `tableView`: The table view that sent the message.
- `oldDescriptors`: An array that contains the previous descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:sortdescriptorsdidchange:))*