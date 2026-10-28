# FoveatedStreamingSession.InputCapability

**Framework**: Foveated Streaming  
**Kind**: enum  
**Role**: Enumeration

An input source that a streaming session can request to send.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
enum InputCapability
```

## Overview

A streaming session declares the input capabilities it needs via [`requestedInputCapabilities`](./requestedinputcapabilities.md).

Input data will only be sent if a user authorizes it. To request authorization, use [`requestAuthorization(for:)`](./requestauthorization%28for%29.md). To understand if an input source is authorized, use [`queryAuthorization(for:)`](./queryauthorization%28for%29.md).

## Topics

### Enumeration Cases
- [FoveatedStreamingSession.InputCapability.accessoryTracking](./inputcapability/accessorytracking.md)
  Accessory tracking input.
- [FoveatedStreamingSession.InputCapability.handTracking](./inputcapability/handtracking.md)
  Hand tracking input.
- [FoveatedStreamingSession.InputCapability.microphone](./inputcapability/microphone.md)
  Microphone input.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/inputcapability)*