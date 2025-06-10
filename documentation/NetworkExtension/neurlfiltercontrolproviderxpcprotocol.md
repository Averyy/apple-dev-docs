# NEURLFilterControlProviderXPCProtocol

**Framework**: Network Extension  
**Kind**: protocol

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
@objc
protocol NEURLFilterControlProviderXPCProtocol : NEAppExtensionXPCProtocol
```

## Topics

### Instance Methods
- [func fetchPrefilterData(reply: (Data?, URL?, String?, UInt32, UInt32, UInt32, (any Error)?) -> Void)](neurlfiltercontrolproviderxpcprotocol/fetchprefilterdata(reply:).md)
- [func start(reply: (Bool, (any Error)?) -> Void)](neurlfiltercontrolproviderxpcprotocol/start(reply:).md)
- [func stop(stopReason: NEProviderStopReason, reply: (Bool, (any Error)?) -> Void)](neurlfiltercontrolproviderxpcprotocol/stop(stopreason:reply:).md)

## Relationships

### Inherits From
- [NEAppExtensionXPCProtocol](neappextensionxpcprotocol.md)
### Conforming Types
- [NEURLFilterControlProviderConfiguration](neurlfiltercontrolproviderconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltercontrolproviderxpcprotocol)*