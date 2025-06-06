# ssid

**Framework**: Core WLAN  
**Kind**: property

The service set identifier (SSID) for the network profile, encoded as a string.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var ssid: String? { get }
```

#### Discussion

If the SSID can not be encoded as a valid UTF-8 or WinLatin1 string, this method returns .

## See Also

- [var security: CWSecurity](cwnetworkprofile/security.md)
  The security mode for the network profile.
- [var ssidData: Data?](cwnetworkprofile/ssiddata.md)
  The service set identifier (SSID) for the network profile, returned as data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/ssid)*