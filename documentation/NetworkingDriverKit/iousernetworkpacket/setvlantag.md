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

The kFeatureHardwareVlan capability, or the case that feature is not enabled, this method should not be used.

## Parameters

- `vlanTag`: To be stored in the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/setvlantag)*