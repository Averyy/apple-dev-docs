# xpcConnection

**Framework**: Network Extension  
**Kind**: property

The XPC connection to the host process.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var xpcConnection: NSXPCConnection?
```

#### Discussion

The framework accesses this property. You don’t need to use it in your app extension.

## See Also

- [func accept(connection: NSXPCConnection) -> Bool](neappextensionconfiguration/accept(connection:).md)
  Accepts incoming XPC connections from the host process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappextensionconfiguration/xpcconnection)*