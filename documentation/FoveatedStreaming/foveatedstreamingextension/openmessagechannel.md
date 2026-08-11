# openMessageChannel(_:)

**Framework**: Foveated Streaming  
**Kind**: method  
**Required**: Yes

Handles a message channel opened by the host app.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func openMessageChannel(_ channel: Self.MessageChannel) throws
```

#### Discussion

The framework vends the [`FoveatedStreamingProviderMessageChannel`](foveatedstreamingprovidermessagechannel.md) and calls this when the host opens a channel.

## Parameters

- `channel`: The channel to service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingextension/openmessagechannel(_:))*