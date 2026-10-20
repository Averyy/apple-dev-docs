# CTCellularDataRestrictedState

**Framework**: Core Telephony  
**Kind**: enum  
**Role**: Enumeration

The possible states of the cellular data policy.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.10+

## Declaration

```swift
enum CTCellularDataRestrictedState
```

```c
enum CTCellularDataRestrictedState : NSUInteger;
```

## Topics

### Constants
- [CTCellularDataRestrictedState.notRestricted](./ctcellulardatarestrictedstate/notrestricted.md)
  A state that allows access to cellular data.
- [CTCellularDataRestrictedState.restricted](./ctcellulardatarestrictedstate/restricted.md)
  A state that denies access to cellular data.
- [CTCellularDataRestrictedState.restrictedStateUnknown](./ctcellulardatarestrictedstate/restrictedstateunknown.md)
  A state whose access to cellular data is unknown.
### Initializers
- [init?(rawValue: UInt)](./ctcellulardatarestrictedstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining the Cellular Data Restricted State
- [var restrictedState: CTCellularDataRestrictedState](./ctcellulardata/restrictedstate.md)
  The current state of cellular data restrictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellulardatarestrictedstate)*