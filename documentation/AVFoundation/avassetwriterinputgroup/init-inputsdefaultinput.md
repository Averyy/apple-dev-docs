# init(inputs:defaultInput:)

**Framework**: AVFoundation  
**Kind**: init

Creates a group for the asset writer inputs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(inputs: [AVAssetWriterInput], defaultInput: AVAssetWriterInput?)
```

#### Discussion

When you add an input group to an asset writer, the system sets the default input’s [`marksOutputTrackAsEnabled`](avassetwriterinput/marksoutputtrackasenabled.md) property value to [`true`](https://developer.apple.com/documentation/Swift/true), and the value of the other inputs in the group to [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `inputs`: The inputs with tracks to arrange into a mutually exclusive group.
- `defaultInput`: The group’s default input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/init(inputs:defaultinput:))*