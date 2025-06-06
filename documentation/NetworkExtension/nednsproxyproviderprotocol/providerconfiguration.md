# providerConfiguration

**Framework**: Network Extension  
**Kind**: property

A dictionary containing vendor-specific configuration parameters for a proxy provider.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var providerConfiguration: [String : Any]? { get set }
```

#### Discussion

This dictionary is passed as-is through the `options` parameter when the framework starts a DNS proxy by calling the proxy’s [`startProxy(options:completionHandler:)`](nednsproxyprovider/startproxy(options:completionhandler:).md) function.

## See Also

- [var providerBundleIdentifier: String?](nednsproxyproviderprotocol/providerbundleidentifier.md)
  A string containing the bundle identifier of the proxy provider to be used by this configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyproviderprotocol/providerconfiguration)*