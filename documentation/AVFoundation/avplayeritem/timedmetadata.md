# timedMetadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of the most recently encountered timed metadata.

**Availability**:
- iOS 4.0+ - Deprecated in 13.0
- iPadOS 4.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: Use [`AVPlayerItemMetadataOutput`](../avplayeritemmetadataoutput.md) to access timed metadata.

## Declaration

```swift
@MainActor
var timedMetadata: [AVMetadataItem]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<AVMetadataItem *> * timedMetadata;
```

#### Return Value

An array of [`AVMetadataItem`](../avmetadataitem.md) or `nil` if no metadata was found.

#### Discussion

Prior to the player item loading its media, this property value is `nil`. You can key-value observe this property to monitor when metadata becomes available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/timedmetadata)*