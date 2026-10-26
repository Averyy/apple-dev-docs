# connection

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the `NSConnection` object that uses the receiver.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (NSConnection *) connection;
```

#### Return Value

The `NSConnection` object that uses the receiver. In an object’s [`encode(with:)`](../nscoding/encode%28with%29.md) method, this is the sending (server) connection. In [`init(coder:)`](../nscoding/init%28coder%29.md) this is the receiving (client) connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportcoder/connection)*