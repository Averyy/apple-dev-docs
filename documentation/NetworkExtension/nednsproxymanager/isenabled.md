# isEnabled

**Framework**: Network Extension  
**Kind**: property

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

#### Discussion

Only one DNS proxy can be active in the system at a time. Therefore, setting this property to [`true`](https://developer.apple.com/documentation/swift/true) disables any DNS proxy configurations of other apps. Similarly, the system sets this property to [`false`](https://developer.apple.com/documentation/swift/false) when any other DNS proxy configuration is enabled.

## See Also

- [var providerProtocol: NEDNSProxyProviderProtocol?](nednsproxymanager/providerprotocol.md)
  The provider-specific portion of the DNS proxy configuration.
- [var localizedDescription: String?](nednsproxymanager/localizeddescription.md)
  A description of the DNS proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/isenabled)*