# userInfo

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An optional user information object associated with the coder.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var userInfo: (any NSObjectProtocol)? { get set }
```

```objc
@property (retain, nullable) id<NSObject> userInfo;
```

## See Also

### Inspecting the Coder
- [var connection: NSXPCConnection?](./connection.md)
  The connection currently performing encoding or decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpccoder/userinfo)*