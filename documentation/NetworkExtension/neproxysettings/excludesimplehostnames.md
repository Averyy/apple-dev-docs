# excludeSimpleHostnames

**Framework**: Network Extension  
**Kind**: property

A Boolean indicating if HTTP requests using single-label host names should be excluded from using the proxy settings.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var excludeSimpleHostnames: Bool { get set }
```

## See Also

- [var exceptionList: [String]?](neproxysettings/exceptionlist.md)
  An array of domain name patterns. If the destination host name of an HTTP connection matches one of these patterns then the proxy settings will not be used for the connection.
- [var matchDomains: [String]?](neproxysettings/matchdomains.md)
  An array of domain strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxysettings/excludesimplehostnames)*