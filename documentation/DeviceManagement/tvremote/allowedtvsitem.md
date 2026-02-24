# TVRemote.AllowedTVsItem

**Framework**: Device Management  
**Kind**: dictionary

The array of valid Apple TV identifiers that the remote can connect to.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
object TVRemote.AllowedTVsItem
```

## Properties

- `TVDeviceID` (string) *(required)*: The MAC address of an Apple TV device that the system permits this iOS device to control. Use the format `xx:xx:xx:xx:xx:xx`, which isn’t case-sensitive.
- `TVDeviceName` (string): The name of an Apple TV device that the system permits this iOS device to control.

## See Also

- [object TVRemote.AllowedRemotesItem](tvremote/allowedremotesitem.md)
  The array of valid devices that Apple TV can connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/tvremote/allowedtvsitem)*