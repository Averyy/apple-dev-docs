# passDescriptions

**Framework**: AVFoundation  
**Kind**: property

An async sequence of pass descriptions to iterate over if multi-pass is supported. This property is nil when multi-pass is not supported.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var passDescriptions: (some AsyncSequence<AVAssetWriterInputPassDescription, Never>)? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/multipasscontroller/passdescriptions)*