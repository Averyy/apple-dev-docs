# AirPlay.PasswordsItem

**Framework**: Device Management  
**Kind**: dictionary

The dictionary that defines passwords for AirPlay destinations.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.10+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AirPlay.PasswordsItem
```

## Properties

- `DeviceID` (string): The device ID of the AirPlay destination; used in macOS. Deprecated in macOS 15 and later as tvOS 18 AirPlay destinations don’t support it; use `DeviceName` instead.
- `DeviceName` (string): The name of the AirPlay destination; used in iOS, and available in macOS 15 and later.
- `Password` (string) *(required)*: The password for the AirPlay destination.

## See Also

- [object AirPlay.AllowListItem](airplay/allowlistitem.md)
  The dictionary that defines allowed destinations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/airplay/passwordsitem)*