# requestAuthorization(for:)

**Framework**: Foveated Streaming  
**Kind**: method

Requests authorization for the given input capabilities, prompting the user for any capability whose status is [`FoveatedStreamingSession.AuthorizationStatus.notDetermined`](foveatedstreamingsession/authorizationstatus/notdetermined.md).

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func requestAuthorization(for inputCapabilities: [FoveatedStreamingSession.InputCapability]) async -> [FoveatedStreamingSession.InputCapability : FoveatedStreamingSession.AuthorizationStatus]
```

#### Return Value

A dictionary mapping each requested capability to its authorization status following the prompt.

#### Discussion

Use this method to drive authorization prompts ahead of [`connect(endpoint:)`](foveatedstreamingsession/connect(endpoint:).md) so apps that want to surface their own pre-flight UI can do so.  At [`connect(endpoint:)`](foveatedstreamingsession/connect(endpoint:).md) time the framework also calls this method automatically for [`requestedInputCapabilities`](foveatedstreamingsession/requestedinputcapabilities.md).

## Parameters

- `inputCapabilities`: The capabilities to authorize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/requestauthorization(for:))*