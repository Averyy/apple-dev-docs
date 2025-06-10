# NEHotspotAuthenticationProviderXPCProtocol

**Framework**: Network Extension  
**Kind**: protocol

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@objc
protocol NEHotspotAuthenticationProviderXPCProtocol : NEAppExtensionXPCProtocol
```

## Topics

### Instance Methods
- [func start(reply: (Bool) -> Void)](nehotspotauthenticationproviderxpcprotocol/start(reply:).md)
- [func stop(stopReason: NEProviderStopReason, reply: (Bool) -> Void)](nehotspotauthenticationproviderxpcprotocol/stop(stopreason:reply:).md)

## Relationships

### Inherits From
- [NEAppExtensionXPCProtocol](neappextensionxpcprotocol.md)
### Conforming Types
- [NEHotspotAuthenticationProviderConfiguration](nehotspotauthenticationproviderconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotauthenticationproviderxpcprotocol)*