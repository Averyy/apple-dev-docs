# WiFi.QoSMarkingPolicy

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that defines the quality-of-service settings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
object WiFi.QoSMarkingPolicy
```

## Properties

- `QoSMarkingAllowListAppIdentifiers` ([string]): An array of app bundle identifiers that defines the allow list for L2 and L3 marking for traffic that goes to the Wi-Fi network. If the array isn’t present, but the `QoSMarkingPolicy` key is present — even empty — no apps can use L2 and L3 marking. Available: iOS 14.5+ | iPadOS 14.5+ | macOS 14+ | tvOS 9+ | visionOS 1+ | watchOS 3.2+
- `QoSMarkingAppleAudioVideoCalls` (boolean): If `true`, adds audio and video traffic of built-in audio or video services, such as FaceTime and Wi-Fi Calling, to the allow list for L2 and L3 marking for traffic that goes to the Wi-Fi network.
- `QoSMarkingEnabled` (boolean): If `true`, disables L3 marking and only uses L2 marking for traffic that goes to the Wi-Fi network. If `false`, the system behaves as if Wi-Fi doesn’t have an association with a Cisco QoS fast lane network.
- `QoSMarkingWhitelistedAppIdentifiers` ([string]): Use `QoSMarkingAllowListAppIdentifiers` instead. Available: iOS 10+ | iPadOS 10+ | macOS 10.13+ | tvOS 9+ | watchOS 3.2+
Deprecated: iOS 14.5+ | iPadOS 14.5+ | macOS 14+

## See Also

- [object WiFi.EAPClientConfiguration](wifi/eapclientconfiguration-data.dictionary.md)
  A dictionary that configures an enterprise network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/wifi/qosmarkingpolicy-data.dictionary)*