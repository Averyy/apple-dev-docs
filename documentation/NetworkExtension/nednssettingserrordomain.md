# NEDNSSettingsErrorDomain

**Framework**: Network Extension  
**Kind**: var

The domain for errors resulting from calls to the DNS settings manager.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
let NEDNSSettingsErrorDomain: String
```

#### Discussion

Match this constant to the [`domain`](https://developer.apple.com/documentation/foundation/nserror/1413924-domain) of an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) encountered when calling methods on [`NEDNSSettingsManager`](nednssettingsmanager.md). The [`NEDNSSettingsManagerError`](nednssettingsmanagererror.md) enumeration defines possible [`code`](https://developer.apple.com/documentation/foundation/nserror/1409165-code) values for these errors.

## See Also

- [enum NEDNSSettingsManagerError](nednssettingsmanagererror.md)
  Error codes specific to DNS managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingserrordomain)*