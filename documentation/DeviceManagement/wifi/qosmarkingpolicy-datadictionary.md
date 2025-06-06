# WiFi.QoSMarkingPolicy

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that defines the quality-of-service settings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.2+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object WiFi.QoSMarkingPolicy
```

#### Discussion

When this dictionary isn’t present for a Wi-Fi network, all apps can use L2 and L3 marking when the Wi-Fi network supports Cisco QoS fast lane. When present in the Wi-Fi payload, the `QoSMarkingPolicy` dictionary needs to contain the list of allowed apps to benefit from L2 and L3 marking.

## See Also

- [object WiFi.EAPClientConfiguration](wifi/eapclientconfiguration-data.dictionary.md)
  A dictionary that configures an enterprise network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/wifi/qosmarkingpolicy-data.dictionary)*