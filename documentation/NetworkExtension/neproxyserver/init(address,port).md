# init(address:port:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

Initialize a newly-allocated `NEProxyServer` object

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(address: String, port: Int)
```

```objc
- (instancetype) initWithAddress:(NSString *) address port:(NSInteger) port;
```

## Parameters

- `address`: The address of the proxy server.
- `port`: The TCP port on which the proxy server is listening for connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxyserver/init(address:port:))*