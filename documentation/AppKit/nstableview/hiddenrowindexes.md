# hiddenRowIndexes

**Framework**: AppKit  
**Kind**: property

The indexes of all hidden table rows.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var hiddenRowIndexes: IndexSet { get }
```

#### Discussion

The value of this property is an index set containing the indexes of any hidden table rows. Table rows may be hidden by invoking the [`hideRows(at:withAnimation:)`](nstableview/hiderows(at:withanimation:).md) method. Some drag-and-drop operations also result in hidden rows.

## See Also

- [func hideRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/hiderows(at:withanimation:).md)
  Hides the specified table rows.
- [func unhideRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/unhiderows(at:withanimation:).md)
  Unhides the specified table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/hiddenrowindexes)*