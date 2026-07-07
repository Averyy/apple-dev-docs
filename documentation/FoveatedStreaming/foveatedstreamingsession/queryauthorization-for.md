# queryAuthorization(for:)

**Framework**: Foveated Streaming  
**Kind**: method

Returns the current authorization status of the given input capabilities without presenting an authorization prompt.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func queryAuthorization(for inputCapabilities: [FoveatedStreamingSession.InputCapability]) async -> [FoveatedStreamingSession.InputCapability : FoveatedStreamingSession.AuthorizationStatus]
```

#### Return Value

A dictionary mapping each queried capability to its current authorization status.

## Parameters

- `inputCapabilities`: The capabilities to query.  Duplicate entries are collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/queryauthorization(for:))*