# localizedDescription

**Framework**: Network Extension  
**Kind**: property

A string that contains the display name of the relay configuration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var localizedDescription: String? { get set }
```

#### Discussion

This string is used as the display name of the relay configuration in the system’s settings UI. If this property is set to `nil` at the time that the configuration is created, it is automatically set to the display name of the calling app.

## See Also

- [var isEnabled: Bool](nerelaymanager/isenabled.md)
  A Boolean used to toggle the enabled state of the relay configuration.
- [var relays: [NERelay]?](nerelaymanager/relays.md)
  An array of one or two relay server configurations. If multiple relays are configured, application traffic routes through both of them in the order they appear in the array.
- [var matchDomains: [String]?](nerelaymanager/matchdomains.md)
  A list of domain strings used to determine which connections will use the relay configuration contained in this object.
- [var excludedDomains: [String]?](nerelaymanager/excludeddomains.md)
  A list of domain strings used to determine which connections won’t use the relay configuration contained in this object.
- [var onDemandRules: [NEOnDemandRule]?](nerelaymanager/ondemandrules.md)
  An array of rules you use to determine which networks the relay uses.
- [class NEOnDemandRule](neondemandrule.md)
  A base class shared by all VPN On Demand rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/localizeddescription)*