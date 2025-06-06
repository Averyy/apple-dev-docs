# lockPasscode

**Framework**: ManagedSettings  
**Kind**: property

A Boolean value that indicates whether to prevent changing the device passcode.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var lockPasscode: Bool? { get set }
```

#### Discussion

If your app doesn’t configure this setting, the value is `nil`.

## See Also

- [static let lockPasscode: SettingMetadata<Bool>](passcodesettings/lockpasscode-swift.type.property.md)
  The metadata for the setting that prevents the user from changing their passcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/passcodesettings/lockpasscode-swift.property)*