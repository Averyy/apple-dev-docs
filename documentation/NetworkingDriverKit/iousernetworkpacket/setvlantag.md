# setVlanTag

**Framework**: NetworkingDriverKit  
**Kind**: method

**Availability**:
- DriverKit 24.0+

## Declaration

```swift
void setVlanTag(uint16_t vlanTag);
```

#### Discussion

Set the Vlan Tag for the packet.

Set the Vlan Tag for the packet, where the driver has enabled the kFeatureHardwareVlan capability, or the case that feature is not enabled, this method should not be used.

## Parameters

- `vlanTag`: To be stored in the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/setvlantag)*