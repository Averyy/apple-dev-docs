# APN.DefaultsData.ApnsItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an APN configuration.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+

## Declaration

```swift
object APN.DefaultsData.ApnsItem
```

## Properties

- `apn` (string) *(required)*: The access point name. Deprecated: iOS 7+ | iPadOS 7+
- `password` (data): The password for the user. For obfuscation purposes, the system encodes the password. If missing, the device prompts for the password during profile installation. Deprecated: iOS 7+ | iPadOS 7+
- `proxy` (string): The IP address or URL of the APN proxy. Deprecated: iOS 7+ | iPadOS 7+
- `proxyPort` (integer): The port number of the APN proxy. Deprecated: iOS 7+ | iPadOS 7+
- `username` (string): The user name. If missing, the device prompts for it during profile installation. Deprecated: iOS 7+ | iPadOS 7+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apn/defaultsdata-data.dictionary/apnsitem)*