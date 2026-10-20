# isEnabled

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The status of a DNS proxy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (getter=isEnabled) BOOL enabled;
```

#### Discussion

Only one DNS proxy can be active in the system at a time. Therefore, setting this property to [`true`](../../Swift/true.md) disables any DNS proxy configurations of other apps. Similarly, the system sets this property to [`false`](../../Swift/false.md) when any other DNS proxy configuration is enabled.

## See Also

### Accessing DNS proxy configuration properties
- [var providerProtocol: NEDNSProxyProviderProtocol?](./providerprotocol.md)
  The provider-specific portion of the DNS proxy configuration.
- [var localizedDescription: String?](./localizeddescription.md)
  A description of the DNS proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/isenabled)*