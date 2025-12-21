# passDescriptions

**Framework**: AVFoundation  
**Kind**: property

An async sequence of pass descriptions to iterate over if multi-pass is supported. This property is nil when multi-pass is not supported.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var passDescriptions: (some AsyncSequence<AVAssetWriterInputPassDescription, Never>)? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/multipasscontroller/passdescriptions)*