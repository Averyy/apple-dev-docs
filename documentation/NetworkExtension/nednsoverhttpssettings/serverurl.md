# serverURL

**Framework**: Network Extension  
**Kind**: property

The URL of a DNS-over-HTTPS server.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var serverURL: URL? { get set }
```

#### Discussion

The URL should use the URI template format defined by [`RFC 8484`](https://developer.apple.comhttps://tools.ietf.org/html/rfc8484), for example `https://dnsserver.example.net/dns-query`.

## See Also

- [init(servers: [String])](nednssettings/init(servers:).md)
  Initialize the `NEDNSSetting` object.
- [var matchDomains: [String]?](nednssettings/matchdomains.md)
  A list of domain strings used to determine which DNS queries will use the DNS resolver settings contained in this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsoverhttpssettings/serverurl)*