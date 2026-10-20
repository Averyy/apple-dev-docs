# requestedInputCapabilities

**Framework**: Foveated Streaming  
**Kind**: property  
**Role**: Instance Property

A list of input data types which should be included as part of the stream.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
@MainActor
final var requestedInputCapabilities: Set<FoveatedStreamingSession.InputCapability> { get set }
```

#### Discussion

The default value is `[]`.

At [`connect(endpoint:)`](./connect%28endpoint%29.md) time, any capability in the requested set with [`FoveatedStreamingSession.AuthorizationStatus.notDetermined`](./authorizationstatus/notdetermined.md) status triggers an authorization prompt before the connection proceeds.  Setting this property does not on its own trigger an authorization prompt — call [`requestAuthorization(for:)`](./requestauthorization%28for%29.md) to do that explicitly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/requestedinputcapabilities)*