# BEProcessCapabilityGrant

**Framework**: BrowserEngineKit  
**Kind**: protocol  
**Role**: Protocol

An object that represents a granted capability.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
@protocol BEProcessCapabilityGrant <NSObject>
```

## Topics

### Testing and changing validity
- [valid](./beprocesscapabilitygrant/valid.md)
  A Boolean value that indicates whether the system grants the capability.
- [- invalidate](./beprocesscapabilitygrant/invalidate.md)
  Revokes access to a capability.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Extension capabilities
- [BEProcessCapability](./beprocesscapability-7av05.md)
  Capabilities of a helper extension process.
- [BEMediaEnvironment](./bemediaenvironment-n91a.md)
  An object that identifies a media playback or streaming environment.
- [class BEWebContentFilter](./bewebcontentfilter.md)
  An object that represents a web content filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beprocesscapabilitygrant)*