# getVlanTag

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit 24.0+

## Declaration

```c
bool getVlanTag(uint16_t *vlanTag) const;
```

#### Return Value

True if the tag is present, false otherwise.

#### Discussion

Get the Vlan Tag from the packet, where the driver has enabled the kFeatureHardwareVlan capability, for the case that feature is not enabled, this method will return false.

## Parameters

- `vlanTag`: Pointer to return vlanTag from the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/getvlantag)*