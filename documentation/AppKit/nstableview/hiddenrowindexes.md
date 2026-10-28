# hiddenRowIndexes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The indexes of all hidden table rows.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var hiddenRowIndexes: IndexSet { get }
```

```objc
@property (copy, readonly) NSIndexSet * hiddenRowIndexes;
```

## Discussion

The value of this property is an index set containing the indexes of any hidden table rows. Table rows may be hidden by invoking the [`hideRows(at:withAnimation:)`](./hiderows%28at,withanimation%29.md) method. Some drag-and-drop operations also result in hidden rows.

## See Also

### Hiding and Showing Table Rows
- [func hideRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./hiderows%28at,withanimation%29.md)
  Hides the specified table rows.
- [func unhideRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./unhiderows%28at,withanimation%29.md)
  Unhides the specified table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/hiddenrowindexes)*