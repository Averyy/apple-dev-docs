# lockESIM

**Framework**: ManagedSettings  
**Kind**: property

A Boolean value that indicates whether to prevent the user from changing their eSIM settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var lockESIM: Bool? { get set }
```

#### Discussion

If your app doesn’t configure this setting, the value is `nil`.

## See Also

- [static let lockESIM: SettingMetadata<Bool>](cellularsettings/lockesim-swift.type.property.md)
  The metadata associated with the constraint that locks the user’s eSIM settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/cellularsettings/lockesim-swift.property)*