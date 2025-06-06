# denyBookstoreErotica

**Framework**: ManagedSettings  
**Kind**: property

A Boolean value that indicates whether to deny media categorized as erotica in the Books store.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var denyBookstoreErotica: Bool? { get set }
```

#### Discussion

Use `denyBookstoreErotica` to deny the user permission to access media with an  tag in the Books store. If your app doesn’t configure this setting, the value is `nil`.

## See Also

- [static let denyBookstoreErotica: SettingMetadata<Bool>](mediasettings/denybookstoreerotica-swift.type.property.md)
  The metadata associated with the setting that denies access to content in the Books store categorized as erotica.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/mediasettings/denybookstoreerotica-swift.property)*