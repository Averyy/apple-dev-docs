# AVAssetWriterInput.MultiPassController

**Framework**: AVFoundation  
**Kind**: class

Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MultiPassController
```

## Topics

### Instance Properties
- [var passDescriptions: (some AsyncSequence<AVAssetWriterInputPassDescription, Never>)?](avassetwriterinput/multipasscontroller/passdescriptions.md)
  An async sequence of pass descriptions to iterate over if multi-pass is supported. This property is nil when multi-pass is not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/multipasscontroller)*