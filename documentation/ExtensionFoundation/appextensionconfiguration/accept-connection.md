# accept(connection:)

**Framework**: ExtensionFoundation  
**Kind**: method  
**Required**: Yes

A method the system calls when a host app tries to connect.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accept(connection: NSXPCConnection) -> Bool
```

#### Return Value

A Boolean value indicating if you are accepting the request.

## Parameters

- `connection`: The connection requesting to connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionconfiguration/accept(connection:))*