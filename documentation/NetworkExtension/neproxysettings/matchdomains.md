# matchDomains

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An array of domain strings.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var matchDomains: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * matchDomains;
```

## Discussion

If the destination host name of a HTTP connection shares a suffix with one of these strings then the proxy settings will be used for the HTTP connection. Otherwise the proxy settings will not be used.

This property should be used in conjunction with a split tunnel VPN, where only certain networks are tunneled by the VPN. The domains of those split tunneling networks should be specified in this property.

## See Also

### Accessing General Proxy Properties
- [var excludeSimpleHostnames: Bool](./excludesimplehostnames.md)
  A Boolean indicating if HTTP requests using single-label host names should be excluded from using the proxy settings.
- [var exceptionList: [String]?](./exceptionlist.md)
  An array of domain name patterns. If the destination host name of an HTTP connection matches one of these patterns then the proxy settings will not be used for the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxysettings/matchdomains)*