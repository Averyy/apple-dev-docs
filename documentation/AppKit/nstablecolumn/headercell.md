# headerCell

**Framework**: AppKit  
**Kind**: property

The cell used to draw the table column’s header.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var headerCell: NSTableHeaderCell { get set }
```

#### Discussion

The value of this property must not be `nil`. It’s recommended that the value of this property be an instance or subclass of [`NSTableHeaderCell`](nstableheadercell.md).

You can set the table column title using the [`title`](nstablecolumn/title.md) property.

## See Also

- [var title: String](nstablecolumn/title.md)
  The title of the table column’s header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/headercell)*