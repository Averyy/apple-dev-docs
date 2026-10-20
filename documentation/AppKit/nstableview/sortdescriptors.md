# sortDescriptors

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The table view’s sort descriptors.

**Availability**:
- macOS

## Declaration

```swift
var sortDescriptors: [NSSortDescriptor] { get set }
```

```objc
@property (copy) NSArray<NSSortDescriptor *> * sortDescriptors;
```

#### Discussion

This property contains an array of [`NSSortDescriptor`](../../Foundation/nssortdescriptor.md) objects. A table column is considered sortable if it has a sort descriptor that specifies the sorting direction, a key to sort by, and a selector defining how to sort. Changing the value of this property may have the side effect of calling the [`tableView(_:sortDescriptorsDidChange:)`](../nstableviewdatasource/tableview%28_,sortdescriptorsdidchange%29.md) method on the table view’s data source.

The contents of this property are archived and persisted along with other column information if autosave is enabled for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/sortdescriptors)*