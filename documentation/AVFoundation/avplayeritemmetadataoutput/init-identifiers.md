# init(identifiers:)

**Framework**: AVFoundation  
**Kind**: init

Creates an instance of AVPlayerItemMetadataOutput.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
init(identifiers: [String]?)
```

#### Return Value

An AVPlayerItemMetadataOutput instance.

#### Discussion

Pass `nil` to receive all of the timed metadata from all enabled `AVPlayerItemTracks` that carry timed metadata.

## Parameters

- `identifiers`: A array of metadata identifiers indicating the metadata items that the output should provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/init(identifiers:))*