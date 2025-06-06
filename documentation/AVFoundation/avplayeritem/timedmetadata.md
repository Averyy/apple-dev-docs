# timedMetadata

**Framework**: AVFoundation  
**Kind**: property

An array of the most recently encountered timed metadata.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var timedMetadata: [AVMetadataItem]? { get }
```

#### Return Value

An array of [`AVMetadataItem`](avmetadataitem.md) or `nil` if no metadata was found.

#### Discussion

Prior to the player item loading its media, this property value is `nil`. You can key-value observe this property to monitor when metadata becomes available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/timedmetadata)*