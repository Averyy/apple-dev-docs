# providerBundleIdentifier

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A string containing the bundle identifier of the proxy provider to be used by this configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var providerBundleIdentifier: String? { get set }
```

```objc
@property (copy, nullable) NSString * providerBundleIdentifier;
```

## See Also

### Accessing the DNS proxy configuration
- [var providerConfiguration: [String : Any]?](./providerconfiguration.md)
  A dictionary containing vendor-specific configuration parameters for a proxy provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyproviderprotocol/providerbundleidentifier)*