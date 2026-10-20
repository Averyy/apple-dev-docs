# CellularDataRestrictionDidUpdateNotifier

**Framework**: Core Telephony  
**Kind**: typealias  
**Role**: Type Alias

A block to provide updates on the app’s cellular data restriction state.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.10+

## Declaration

```swift
typealias CellularDataRestrictionDidUpdateNotifier = (CTCellularDataRestrictedState) -> Void
```

```c
typedef void (^)(enum CTCellularDataRestrictedState) CellularDataRestrictionDidUpdateNotifier;
```

## See Also

### Handling Policy Changes
- [var cellularDataRestrictionDidUpdateNotifier: CellularDataRestrictionDidUpdateNotifier?](./ctcellulardata/cellulardatarestrictiondidupdatenotifier.md)
  A block that handles cellular data restriction state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cellulardatarestrictiondidupdatenotifier)*