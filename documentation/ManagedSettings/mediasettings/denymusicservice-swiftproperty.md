# denyMusicService

**Framework**: ManagedSettings  
**Kind**: property

A Boolean value that indicates whether to prevent the user from accessing Apple Music’s streaming content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var denyMusicService: Bool? { get set }
```

#### Discussion

If you set this value to `true`, the Music app reverts to classic mode. If your app doesn’t configure this setting, the value is `nil`.

## See Also

- [static let denyMusicService: SettingMetadata<Bool>](mediasettings/denymusicservice-swift.type.property.md)
  The metadata associated with denying access to Apple Music.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/mediasettings/denymusicservice-swift.property)*