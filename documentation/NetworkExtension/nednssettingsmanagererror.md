# NEDNSSettingsManagerError

**Framework**: Network Extension  
**Kind**: enum

Error codes specific to DNS managers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum NEDNSSettingsManagerError
```

## Topics

### Error codes
- [NEDNSSettingsManagerError.configurationInvalid](nednssettingsmanagererror/configurationinvalid.md)
  An error code that indicates the DNS settings manager is invalid.
- [NEDNSSettingsManagerError.configurationDisabled](nednssettingsmanagererror/configurationdisabled.md)
  An error code that indicates the DNS settings manager isn’t enabled.
- [NEDNSSettingsManagerError.configurationStale](nednssettingsmanagererror/configurationstale.md)
  An error code that indicates the DNS settings manager isn’t loaded.
- [NEDNSSettingsManagerError.configurationCannotBeRemoved](nednssettingsmanagererror/configurationcannotberemoved.md)
  An error code that indicates removing the DNS settings manager failed.
### Initializers
- [init?(rawValue: Int)](nednssettingsmanagererror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let NEDNSSettingsErrorDomain: String](nednssettingserrordomain.md)
  The domain for errors resulting from calls to the DNS settings manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanagererror)*