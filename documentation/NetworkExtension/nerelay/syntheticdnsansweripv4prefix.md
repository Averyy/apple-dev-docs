# syntheticDNSAnswerIPv4Prefix

**Framework**: Network Extension  
**Kind**: property

An IPv4 address prefix the relay uses to handle address info requests.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var syntheticDNSAnswerIPv4Prefix: String? { get set }
```

#### Discussion

The value of this property is an address prefix, such as `192.0.2.0/24`. The relay manager uses this prefix to synthesize DNS answers for apps that use `getaddrinfo()` to resolve domains included in [`matchDomains`](nerelaymanager/matchdomains.md).

## See Also

- [var additionalHTTPHeaderFields: [String : String]](nerelay/additionalhttpheaderfields.md)
  A dictionary of additional HTTP headers to send as part of `CONNECT` requests to the relay.
- [var identityData: Data?](nerelay/identitydata.md)
  The PKCS12 data for the relay client authentication.
- [var identityDataPassword: String?](nerelay/identitydatapassword.md)
  The password the relay uses to decrypt the PKCS12 identity data.
- [var syntheticDNSAnswerIPv6Prefix: String?](nerelay/syntheticdnsansweripv6prefix.md)
  An IPv6 address prefix the relay uses to handle address info requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelay/syntheticdnsansweripv4prefix)*