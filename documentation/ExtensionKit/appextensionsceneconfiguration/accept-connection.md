# accept(connection:)

**Framework**: ExtensionKit  
**Kind**: method

A closure the framework calls when a host tries to connect to this extension.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accept(connection: NSXPCConnection) -> Bool
```

#### Return Value

A Boolean value that indicates whether the extension accepts the connection.

#### Discussion

- connection: The incoming XPC connection object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionsceneconfiguration/accept(connection:))*