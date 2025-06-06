# Ethernet Bond Aggregation Status

**Framework**: System Configuration

Ethernet bond aggregation status codes.

## Topics

### Constants
- [var kSCBondStatusOK: Int](kscbondstatusok.md)
  The status is valid (for example, enabled, active, running, and so on).
- [var kSCBondStatusLinkInvalid: Int](kscbondstatuslinkinvalid.md)
  The link state is not valid (such as down, half-duplex, or wrong speed).
- [var kSCBondStatusNoPartner: Int](kscbondstatusnopartner.md)
  The port on the switch to which the device is connected doesn’t seem to have 802.3ad Link Aggregation enabled.
- [var kSCBondStatusNotInActiveGroup: Int](kscbondstatusnotinactivegroup.md)
  Communication with a partner is occurring, but the link aggregation group is different from the one that is active.
- [var kSCBondStatusUnknown: Int](kscbondstatusunknown.md)
  Nonspecific failure.

## See Also

- [Ethernet Bond Status Constants](ethernet-bond-status-constants.md)
  Ethernet bond status codes.
- [Network Interface Types](network-interface-types.md)
  Keys that identify network interface types.
- [Network Protocol Types](network-protocol-types.md)
  Keys that identify network protocol types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/1546981-ethernet-bond-aggregation-status)*