# NETunnelProviderError.Code

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

Error codes that the tunnel provider declares.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum NETunnelProviderError : NSInteger;
```

## Topics

### Error codes
- [NETunnelProviderError.Code.networkSettingsInvalid](./code/networksettingsinvalid.md)
  The provided tunnel network settings are invalid.
- [NETunnelProviderError.Code.networkSettingsCanceled](./code/networksettingscanceled.md)
  The request to set or clear the tunnel network settings was canceled.
- [NETunnelProviderError.Code.networkSettingsFailed](./code/networksettingsfailed.md)
  The request to set or clear the tunnel network settings failed.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidererror-swift.struct/code)*