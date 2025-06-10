# accept(connection:)

**Framework**: Network Extension  
**Kind**: method

Accepts incoming XPC connections from the host process.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func accept(connection: NSXPCConnection) -> Bool
```

#### Discussion

The framework calls this method. You don’t need to call it in your app extension.

## Parameters

- `connection`: The incoming XPC connection.

## See Also

- [var xpcConnection: NSXPCConnection?](neappextensionconfiguration/xpcconnection.md)
  The XPC connection to the host process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappextensionconfiguration/accept(connection:))*