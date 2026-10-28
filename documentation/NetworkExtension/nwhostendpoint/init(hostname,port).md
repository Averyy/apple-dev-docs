# init(hostname:port:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

Create a host endpoint with a hostname and port.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_endpoint_create_host(_:_:)`](../../Network/nw_endpoint_create_host%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
convenience init(hostname: String, port: String)
```

```objc
+ (instancetype) endpointWithHostname:(NSString *) hostname port:(NSString *) port;
```

## Discussion

If the hostname is a domain name, such as `www.example.com`, starting a connection to the host endpoint causes the hostname to be resolved to an address during the connection process. If the hostname is an IPv4 or IPv6 address, such as `10.0.0.1` or `fe80::1`, starting a connection to the host endpoint will cause the address to be used directly.

## Parameters

- `hostname`: A string representation of the hostname or address, such as `www.example.com` or `10.0.0.1`.
- `port`: A string containing the port on the host, such as `80`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwhostendpoint/init(hostname:port:))*