# CTCellularData

**Framework**: Core Telephony  
**Kind**: class

An object indicating whether the app can access cellular data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CTCellularData
```

#### Overview

This property represents all access to cellular data. If the [`restrictedState`](ctcellulardata/restrictedstate.md) is [`CTCellularDataRestrictedState.restricted`](ctcellulardatarestrictedstate/restricted.md), the app cannot use the cellular network.

## Topics

### Determining the Cellular Data Restricted State
- [var restrictedState: CTCellularDataRestrictedState](ctcellulardata/restrictedstate.md)
  The current state of cellular data restrictions.
- [enum CTCellularDataRestrictedState](ctcellulardatarestrictedstate.md)
  The possible states of the cellular data policy.
### Handling Policy Changes
- [var cellularDataRestrictionDidUpdateNotifier: CellularDataRestrictionDidUpdateNotifier?](ctcellulardata/cellulardatarestrictiondidupdatenotifier.md)
  A block that handles cellular data restriction state changes.
- [typealias CellularDataRestrictionDidUpdateNotifier](cellulardatarestrictiondidupdatenotifier.md)
  A block to provide updates on the app’s cellular data restriction state.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellulardata)*