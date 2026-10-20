# providerConfiguration

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSDictionary<NSString *,id> * providerConfiguration;
```

#### Discussion

This dictionary is passed as-is through the `options` parameter when the framework starts a DNS proxy by calling the proxy’s [`startProxy(options:completionHandler:)`](../nednsproxyprovider/startproxy%28options,completionhandler%29.md) function.

## See Also

### Accessing the DNS proxy configuration
- [var providerBundleIdentifier: String?](./providerbundleidentifier.md)
  A string containing the bundle identifier of the proxy provider to be used by this configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyproviderprotocol/providerconfiguration)*