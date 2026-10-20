# kSCBondStatusLinkInvalid

**Framework**: System Configuration  
**Kind**: var  
**Role**: Global Variable

The link state is not valid (such as down, half-duplex, or wrong speed).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var kSCBondStatusLinkInvalid: Int { get }
```

```c
kSCBondStatusLinkInvalid
```

## See Also

### Constants
- [var kSCBondStatusOK: Int](./kscbondstatusok.md)
  The status is valid (for example, enabled, active, running, and so on).
- [var kSCBondStatusNoPartner: Int](./kscbondstatusnopartner.md)
  The port on the switch to which the device is connected doesn’t seem to have 802.3ad Link Aggregation enabled.
- [var kSCBondStatusNotInActiveGroup: Int](./kscbondstatusnotinactivegroup.md)
  Communication with a partner is occurring, but the link aggregation group is different from the one that is active.
- [var kSCBondStatusUnknown: Int](./kscbondstatusunknown.md)
  Nonspecific failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/kscbondstatuslinkinvalid)*