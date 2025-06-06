# denyExplicitContent

**Framework**: ManagedSettings  
**Kind**: property

A Boolean value that indicates whether to prevent the user from accessing explicit content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var denyExplicitContent: Bool? { get set }
```

#### Discussion

Use `denyExplicitContent` to hide music and video content that has an  tag. If your app doesn’t configure this setting, the value is `nil`.

## See Also

- [static let denyExplicitContent: SettingMetadata<Bool>](mediasettings/denyexplicitcontent-swift.type.property.md)
  The metadata for the setting that denies explicit content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/mediasettings/denyexplicitcontent-swift.property)*