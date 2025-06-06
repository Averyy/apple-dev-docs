# denyAutoFill

**Framework**: ManagedSettings  
**Kind**: property

A Boolean value that indicates whether Safari’s AutoFill feature is active.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var denyAutoFill: Bool? { get set }
```

#### Discussion

Set this value to `true` to prevent Safari from automatically entering passwords, contact information, and credit cards in form fields. This value also denies Safari permission to use the keychain to AutoFill stored credentials. If your app doesn’t configure this setting, the value is `nil`.

## See Also

- [static let denyAutoFill: SettingMetadata<Bool>](safarisettings/denyautofill-swift.type.property.md)
  The metadata associated with the setting that deactivates Safari’s AutoFill feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/safarisettings/denyautofill-swift.property)*