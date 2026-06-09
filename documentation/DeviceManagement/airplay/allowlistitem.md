# AirPlay.AllowListItem

**Framework**: Device Management  
**Kind**: dictionary

The dictionary that defines allowed destinations.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.10+

## Declaration

```swift
object AirPlay.AllowListItem
```

## Properties

- `DeviceID` (string): The device ID of the AirPlay destination in the format `xx:xx:xx:xx:xx:xx`. This field isn’t case-sensitive. The system limits the list of visible AirPlay destinations to devices that are present in the `AllowList` field of all installed AirPlay payloads. Specifying the same MACAddress more than once, whether in the same payload across different payloads, results in undefined behavior. As of tvOS 18, `DeviceID` isn’t supported. Deprecated: iOS 18+ | iPadOS 18+ | macOS 15+
- `DeviceName` (string): The name of the AirPlay device. The system limits the list of visible AirPlay destinations to devices that are present in the `AllowList` field of all installed AirPlay payloads. Available: iOS 18+ | iPadOS 18+ | macOS 15+
Deprecated: iOS 14.5+ | iPadOS 14.5+ | macOS 11.3+

## See Also

- [object AirPlay.PasswordsItem](airplay/passwordsitem.md)
  The dictionary that defines passwords for AirPlay destinations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/airplay/allowlistitem)*