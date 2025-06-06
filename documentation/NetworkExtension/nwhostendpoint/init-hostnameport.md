# init(hostname:port:)

**Framework**: Network Extension  
**Kind**: init

Create a host endpoint with a hostname and port.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(hostname: String, port: String)
```

#### Discussion

If the hostname is a domain name, such as `www.example.com`, starting a connection to the host endpoint causes the hostname to be resolved to an address during the connection process. If the hostname is an IPv4 or IPv6 address, such as `10.0.0.1` or `fe80::1`, starting a connection to the host endpoint will cause the address to be used directly.

## Parameters

- `hostname`: A string representation of the hostname or address, such as   or  .
- `port`: A string containing the port on the host, such as  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwhostendpoint/init(hostname:port:))*