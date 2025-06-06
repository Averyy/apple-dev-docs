# cellularDataRestrictionDidUpdateNotifier

**Framework**: Core Telephony  
**Kind**: property

A block that handles cellular data restriction state changes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var cellularDataRestrictionDidUpdateNotifier: CellularDataRestrictionDidUpdateNotifier? { get set }
```

#### Discussion

The system executes this block when the app first sets the callback handler, and then every time the cellular data allowed policy changes. Execution of the block occurs on the default priority global dispatch queue.

## See Also

- [typealias CellularDataRestrictionDidUpdateNotifier](cellulardatarestrictiondidupdatenotifier.md)
  A block to provide updates on the app’s cellular data restriction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellulardata/cellulardatarestrictiondidupdatenotifier)*