# ssidData

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Instance Property

The service set identifier (SSID) for the network profile, returned as data.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var ssidData: Data? { get }
```

```objc
@property (copy, readonly, nullable) NSData * ssidData;
```

## Discussion

The SSID is 1-32 octets.

## See Also

### Instance Properties
- [var security: CWSecurity](./security.md)
  The security mode for the network profile.
- [var ssid: String?](./ssid.md)
  The service set identifier (SSID) for the network profile, encoded as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/ssiddata)*