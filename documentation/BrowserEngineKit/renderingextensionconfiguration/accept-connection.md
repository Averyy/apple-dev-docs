# accept(connection:)

**Framework**: BrowserEngineKit  
**Kind**: method

A method the system calls when a host app tries to connect.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

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

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/renderingextensionconfiguration/accept(connection:))*