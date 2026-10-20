# connection

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The connection currently performing encoding or decoding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var connection: NSXPCConnection? { get }
```

```objc
@property (strong, readonly, nullable) NSXPCConnection * connection;
```

## See Also

### Inspecting the Coder
- [var userInfo: (any NSObjectProtocol)?](./userinfo.md)
  An optional user information object associated with the coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpccoder/connection)*