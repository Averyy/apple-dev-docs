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
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object WiFi.QoSMarkingPolicy
```

## Properties

- `QoSMarkingAllowListAppIdentifiers` ([string]): An array of app bundle identifiers that defines the allow list for L2 and L3 marking for traffic that goes to the Wi-Fi network. If the array isn’t present, but the `QoSMarkingPolicy` key is present — even empty — no apps can use L2 and L3 marking. Available in iOS 14.5 and later, macOS 14 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `QoSMarkingAppleAudioVideoCalls` (boolean): If `true`, adds audio and video traffic of built-in audio or video services, such as FaceTime and Wi-Fi Calling, to the allow list for L2 and L3 marking for traffic that goes to the Wi-Fi network. Available in iOS 10 and later, macOS 10.13 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `QoSMarkingEnabled` (boolean): If `true`, disables L3 marking and only uses L2 marking for traffic that goes to the Wi-Fi network. If `false`, the system behaves as if Wi-Fi doesn’t have an association with a Cisco QoS fast lane network. Available in iOS 10 and later, macOS 10.13 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `QoSMarkingWhitelistedAppIdentifiers` ([string]): Use `QoSMarkingAllowListAppIdentifiers` instead. Available in iOS 10 and later, macOS 10.13 and later, tvOS 9 and later, and watchOS 3.2 and later. Deprecated in iOS 14.5 and later, and macOS 14 and later.

## See Also

- [object WiFi.EAPClientConfiguration](wifi/eapclientconfiguration-data.dictionary.md)
  A dictionary that configures an enterprise network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/wifi/qosmarkingpolicy-data.dictionary)*