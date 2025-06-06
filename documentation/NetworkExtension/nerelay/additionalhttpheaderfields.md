# additionalHTTPHeaderFields

**Framework**: Network Extension  
**Kind**: property

A dictionary of additional HTTP headers to send as part of `CONNECT` requests to the relay.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var additionalHTTPHeaderFields: [String : String] { get set }
```

## See Also

- [var identityData: Data?](nerelay/identitydata.md)
  The PKCS12 data for the relay client authentication.
- [var identityDataPassword: String?](nerelay/identitydatapassword.md)
  The password the relay uses to decrypt the PKCS12 identity data.
- [var syntheticDNSAnswerIPv4Prefix: String?](nerelay/syntheticdnsansweripv4prefix.md)
  An IPv4 address prefix the relay uses to handle address info requests.
- [var syntheticDNSAnswerIPv6Prefix: String?](nerelay/syntheticdnsansweripv6prefix.md)
  An IPv6 address prefix the relay uses to handle address info requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelay/additionalhttpheaderfields)*