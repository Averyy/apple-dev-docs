# RequestMirroringCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to prompt the user to share their screen using AirPlay Mirroring.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.10+

## Declaration

```swift
object RequestMirroringCommand.Command
```

## Properties

- `DestinationDeviceID` (string): The hardware address of the AirPlay Mirroring destination that identifies the device, in the format `xx:xx:xx:xx:xx`. This value isn’t case-sensitive. Not available for Apple TV devices running tvOS 18 or later, use `DestinationName` instead.
- `DestinationName` (string): The name of the AirPlay Mirroring destination.
- `Password` (string): The screen-sharing password that the device uses when connecting to the destination.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.
- `ScanTime` (integer): The number of seconds, from `10` to `300`, for the device to spend searching for the destination. The default value is `30`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/requestmirroringcommand/command-data.dictionary)*