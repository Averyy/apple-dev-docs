# getVlanTag

**Framework**: NetworkingDriverKit  
**Kind**: method

**Availability**:
- DriverKit 24.0+

## Declaration

```swift
bool getVlanTag(uint16_t * vlanTag) const;
```

#### Return Value

True if the tag is present, false otherwise.

#### Discussion

The kFeatureHardwareVlan capability, for the case that feature is not enabled, this method will return false.

## Parameters

- `vlanTag`: Pointer to return vlanTag from the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket/getvlantag)*