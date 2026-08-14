# FoveatedStreamingSession.InputCapability

**Framework**: Foveated Streaming  
**Kind**: enum

An input source that a streaming session can request to send.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum InputCapability
```

#### Overview

A streaming session declares the input capabilities it needs via [`requestedInputCapabilities`](foveatedstreamingsession/requestedinputcapabilities.md).

Input data will only be sent if a user authorizes it. To request authorization, use [`requestAuthorization(for:)`](foveatedstreamingsession/requestauthorization(for:).md). To understand if an input source is authorized, use [`queryAuthorization(for:)`](foveatedstreamingsession/queryauthorization(for:).md).

## Topics

### Enumeration Cases
- [FoveatedStreamingSession.InputCapability.accessoryTracking](foveatedstreamingsession/inputcapability/accessorytracking.md)
  Accessory tracking input.
- [FoveatedStreamingSession.InputCapability.handTracking](foveatedstreamingsession/inputcapability/handtracking.md)
  Hand tracking input.
- [FoveatedStreamingSession.InputCapability.microphone](foveatedstreamingsession/inputcapability/microphone.md)
  Microphone input.

## Relationships

### Conforms To
- [CaseIterable](../swift/caseiterable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/inputcapability)*