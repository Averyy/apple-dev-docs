# NEDNSSettingsErrorDomain

**Framework**: Network Extension  
**Kind**: var  
**Role**: Global Variable

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

```c
extern NSString * const NEDNSSettingsErrorDomain;
```

## Discussion

Match this constant to the [`domain`](../Foundation/nserror/domain.md) of an [`NSError`](../Foundation/nserror.md) encountered when calling methods on [`NEDNSSettingsManager`](./nednssettingsmanager.md). The [`NEDNSSettingsManagerError`](./nednssettingsmanagererror.md) enumeration defines possible [`code`](../Foundation/nserror/code.md) values for these errors.

## See Also

### Handling errors
- [enum NEDNSSettingsManagerError](./nednssettingsmanagererror.md)
  Error codes specific to DNS managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingserrordomain)*