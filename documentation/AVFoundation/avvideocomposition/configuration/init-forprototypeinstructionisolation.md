# init(for:prototypeInstruction:isolation:)

**Framework**: AVFoundation  
**Kind**: init

Initializes a video composition configuration with the specified asset properties and optional prototype video composition instruction.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(for asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction? = nil, isolation: isolated (any Actor)? = #isolation) async throws
```

## Parameters

- `asset`: Asset to use with the video composition
- `prototypeInstruction`: A video composition instruction to use as a prototype.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration/init(for:prototypeinstruction:isolation:))*