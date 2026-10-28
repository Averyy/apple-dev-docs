# serverName

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The TLS name of a DNS-over-TLS server.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var serverName: String? { get set }
```

```objc
@property (copy, nullable) NSString * serverName;
```

## Discussion

The server will be accessed over TCP port 853, as defined in [RFC 7858](https://tools.ietf.org/html/rfc7858). The server name is used for TLS validation.

## See Also

### Configuring server properties
- [init(servers: [String])](../nednssettings/init%28servers%29.md)
  Initialize the `NEDNSSetting` object.
- [var matchDomains: [String]?](../nednssettings/matchdomains.md)
  A list of domain strings used to determine which DNS queries will use the DNS resolver settings contained in this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsovertlssettings/servername)*