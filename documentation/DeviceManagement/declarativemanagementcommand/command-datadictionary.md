# DeclarativeManagementCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to enable the declarative management engine on a device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DeclarativeManagementCommand.Command
```

#### Discussion

The server uses this command to turn on the declarative management engine on the device the first time the server sends it. Subsequent commands trigger a declarative management synchronization operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarativemanagementcommand/command-data.dictionary)*