# dnsSettings

**Framework**: Network Extension  
**Kind**: property

An object that contains the configuration settings for a DNS server.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var dnsSettings: NEDNSSettings? { get set }
```

#### Discussion

This property can be set to either an [`NEDNSOverHTTPSSettings`](nednsoverhttpssettings.md) object or an [`NEDNSOverTLSSettings`](nednsovertlssettings.md) object.

## See Also

- [var isEnabled: Bool](nednssettingsmanager/isenabled.md)
  A Boolean you use to query the enabled state of the DNS settings configuration.
- [var localizedDescription: String?](nednssettingsmanager/localizeddescription.md)
  A string that contains the display name of the DNS settings configuration.
- [var onDemandRules: [NEOnDemandRule]?](nednssettingsmanager/ondemandrules.md)
  A list of ordered rules that defines the networks on which the DNS settings will apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/dnssettings)*