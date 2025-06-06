# localizedDescription

**Framework**: Network Extension  
**Kind**: property

A string that contains the display name of the DNS settings configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var localizedDescription: String? { get set }
```

#### Discussion

This string is used as the display name of the DNS settings configuration in the system’s settings UI. If this property is set to `nil` at the time that the configuration is created, it is automatically set to the display name of the calling app.

## See Also

- [var isEnabled: Bool](nednssettingsmanager/isenabled.md)
  A Boolean you use to query the enabled state of the DNS settings configuration.
- [var dnsSettings: NEDNSSettings?](nednssettingsmanager/dnssettings.md)
  An object that contains the configuration settings for a DNS server.
- [var onDemandRules: [NEOnDemandRule]?](nednssettingsmanager/ondemandrules.md)
  A list of ordered rules that defines the networks on which the DNS settings will apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/localizeddescription)*