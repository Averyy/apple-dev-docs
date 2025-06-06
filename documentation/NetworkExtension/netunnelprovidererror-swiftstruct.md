# NETunnelProviderError

**Framework**: Network Extension  
**Kind**: struct

An error that the tunnel provider encounters.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct NETunnelProviderError
```

## Topics

### Error information
- [NETunnelProviderError.Code](netunnelprovidererror-swift.struct/code.md)
  Error codes that the tunnel provider declares.
### Error codes
- [static var networkSettingsInvalid: NETunnelProviderError.Code](netunnelprovidererror-swift.struct/networksettingsinvalid.md)
  The provided tunnel network settings are invalid.
- [static var networkSettingsCanceled: NETunnelProviderError.Code](netunnelprovidererror-swift.struct/networksettingscanceled.md)
  The request to set or clear the tunnel network settings was canceled.
- [static var networkSettingsFailed: NETunnelProviderError.Code](netunnelprovidererror-swift.struct/networksettingsfailed.md)
  The request to set or clear the tunnel network settings failed.
### Type Properties
- [static var errorDomain: String](netunnelprovidererror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidererror-swift.struct)*