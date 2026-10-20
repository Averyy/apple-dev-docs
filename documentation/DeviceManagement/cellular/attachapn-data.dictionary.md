# Cellular.AttachAPN

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A dictionary that contains details about an attach access point name (APN) configuration.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- watchOS 3.2+

## Declaration

```
object Cellular.AttachAPN
```

## Properties

- `AllowedProtocolMask` (integer): The Internet Protocol versions that the system supports. Allowed values:

  - `1`: IPv4
  - `2`: IPv6
  - `3`: Both

  Available: iOS 10.3+ | iPadOS 10.3+ | watchOS 3.2+

  **Allowed Values**: `1`, `2`, `3`
- `AuthenticationType` (string): The authentication type.

  **Default**: `PAP`; **Allowed Values**: `CHAP`, `PAP`
- `Name` (string) *(required)*: The name for this configuration.
- `Password` (string): The password for the user.
- `Username` (string): The user name.

## See Also

### Objects
- [object Cellular.APNsItem](./apnsitem.md)
  A dictionary that contains details about an access point name (APN) configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/cellular/attachapn-data.dictionary)*