# TVRemote.AllowedRemotesItem

**Framework**: Device Management  
**Kind**: dictionary

The array of valid devices that Apple TV can connect to.

**Availability**:
- tvOS 11.3+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object TVRemote.AllowedRemotesItem
```

## Properties

- `RemoteDeviceID` (string) *(required)*: The MAC address of a permitted iOS device that can control this Apple TV. Use the format `xx:xx:xx:xx:xx:xx`, which isn’t case-sensitive.

## See Also

- [object TVRemote.AllowedTVsItem](tvremote/allowedtvsitem.md)
  The array of valid Apple TV identifiers that the remote can connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/tvremote/allowedremotesitem)*