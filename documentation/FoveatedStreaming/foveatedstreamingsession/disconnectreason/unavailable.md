# unavailable

**Framework**: Foveated Streaming  
**Kind**: property

A disconnect reason indicating the foveated streaming service is currently unavailable.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
static var unavailable: FoveatedStreamingSession.DisconnectReason { get }
```

#### Discussion

This disconnect reason can occur if another app on the system is already streaming.  Inform people to close other apps and try again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/disconnectreason/unavailable)*