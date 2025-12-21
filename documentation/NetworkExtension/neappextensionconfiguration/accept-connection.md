# accept(connection:)

**Framework**: Network Extension  
**Kind**: method

Accepts incoming XPC connections from the host process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func accept(connection: NSXPCConnection) -> Bool
```

#### Discussion

The framework calls this method. You don’t need to call it in your app extension.

## Parameters

- `connection`: The incoming XPC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappextensionconfiguration/accept(connection:))*