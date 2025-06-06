# sortDescriptorPrototype

**Framework**: AppKit  
**Kind**: property

The table column’s sort descriptor prototype.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
@MainActor var sortDescriptorPrototype: NSSortDescriptor? { get set }
```

#### Discussion

A table column is considered sortable if it has a sort descriptor that specifies the sorting direction, a key to sort by, and a selector that defines how to sort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/sortdescriptorprototype)*