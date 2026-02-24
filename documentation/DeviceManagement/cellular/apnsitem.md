# Cellular.APNsItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains details about an access point name (APN) configuration.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- watchOS 3.2+

## Declaration

```swift
object Cellular.APNsItem
```

## Properties

- `AllowedProtocolMask` (integer): The Internet Protocol versions that the system supports. Available in iOS 10.3 and later. Allowed values: - `1`: IPv4
- `2`: IPv6
- `3`: Both
- `AllowedProtocolMaskInDomesticRoaming` (integer): The Internet Protocol versions that the system supports while roaming. Available in iOS 10.3 and later. Allowed values: - `1`: IPv4
- `2`: IPv6
- `3`: Both
- `AllowedProtocolMaskInRoaming` (integer): The Internet Protocol versions that the system supports while roaming. Available in iOS 10.3 and later. Allowed values: - `1`: IPv4
- `2`: IPv6
- `3`: Both
- `AuthenticationType` (string): The authentication type for logging in.
- `DefaultProtocolMask` (integer): The default Internet Protocol versions. Available in iOS 10.3 but no longer used in iOS 11 and later. Allowed values: - `1`: IPv4
- `2`: IPv6
- `3`: Both
- `EnableXLAT464` (boolean): If `true`, the system enables XLAT464. Available in iOS 16 and later and watchOS 9 and later.
- `Name` (string) *(required)*: The name for this configuration.
- `Password` (string): The user’s password for the APN.
- `ProxyPort` (integer): The proxy server’s port number.
- `ProxyServer` (string): The proxy server’s address.
- `Username` (string): The user name for the APN.

## See Also

- [object Cellular.AttachAPN](cellular/attachapn-data.dictionary.md)
  A dictionary that contains details about an attach access point name (APN) configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/cellular/apnsitem)*