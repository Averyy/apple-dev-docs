# DeclarativeManagementCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to enable your server to support declarative management or trigger a declarative management synchronization operation on the device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object DeclarativeManagementCommand.Command
```

## Properties

- `Data` (data): The base64-encoded declarative management JSON request using a [`TokensResponse`](tokensresponse.md).
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarativemanagementcommand/command-data.dictionary)*