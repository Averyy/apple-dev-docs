# FoveatedStreamingProviderStatus.disconnected(error:)

**Framework**: Foveated Streaming  
**Kind**: case

The session has been disconnected for the provided reason.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
case disconnected(error: NSError?)
```

#### Discussion

If `error` is `nil`, then the disconnect event was requested by calling [`disconnect()`](foveatedstreamingextension/disconnect().md).

If `error` is non-`nil`, then the disconnect event was due to an unexpected error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderstatus/disconnected(error:))*