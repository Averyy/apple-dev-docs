# DisableRemoteDesktopCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to disable Remote Desktop on a device.

**Availability**:
- macOS 10.14.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DisableRemoteDesktopCommand
```

## Topics

### Objects
- [object DisableRemoteDesktopCommand.Command](disableremotedesktopcommand/command-data.dictionary.md)
  The command to disable Remote Desktop on a device.

## Properties

- `Command` (DisableRemoteDesktopCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object DisableRemoteDesktopResponse](disableremotedesktopresponse.md)
  A response from the device after it processes the command to disable Remote Desktop on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disableremotedesktopcommand)*