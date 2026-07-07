# requestedInputCapabilities

**Framework**: Foveated Streaming  
**Kind**: property

A list of input data types which should be included as part of the stream.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final var requestedInputCapabilities: Set<FoveatedStreamingSession.InputCapability> { get set }
```

#### Discussion

The default value is `[]`.

At [`connect(endpoint:)`](foveatedstreamingsession/connect(endpoint:).md) time, any capability in the requested set with [`FoveatedStreamingSession.AuthorizationStatus.notDetermined`](foveatedstreamingsession/authorizationstatus/notdetermined.md) status triggers an authorization prompt before the connection proceeds.  Setting this property does not on its own trigger an authorization prompt — call [`requestAuthorization(for:)`](foveatedstreamingsession/requestauthorization(for:).md) to do that explicitly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/requestedinputcapabilities)*