# AirPlay.PasswordsItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The dictionary that defines passwords for AirPlay destinations.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.10+

## Declaration

```
object AirPlay.PasswordsItem
```

## Properties

- `DeviceID` (string) *(deprecated)*: The device ID of the AirPlay destination; used in macOS.

  Deprecated in macOS 15 and later as tvOS 18 AirPlay destinations don’t support it; use `DeviceName` instead.

  Available: macOS 10.10+
  Deprecated: macOS 15+
- `DeviceName` (string): The name of the AirPlay destination.

  Available: iOS 7+ | iPadOS 7+ | macOS 15+
- `Password` (string) *(required)*: The password for the AirPlay destination.

## See Also

### Objects
- [object AirPlay.AllowListItem](./allowlistitem.md)
  The dictionary that defines allowed destinations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/airplay/passwordsitem)*