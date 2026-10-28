# exceptionList

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An array of domain name patterns. If the destination host name of an HTTP connection matches one of these patterns then the proxy settings will not be used for the connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var exceptionList: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * exceptionList;
```

## Discussion

The pattern strings may contain ‘*’ characters as wildcards.

## See Also

### Accessing General Proxy Properties
- [var excludeSimpleHostnames: Bool](./excludesimplehostnames.md)
  A Boolean indicating if HTTP requests using single-label host names should be excluded from using the proxy settings.
- [var matchDomains: [String]?](./matchdomains.md)
  An array of domain strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxysettings/exceptionlist)*