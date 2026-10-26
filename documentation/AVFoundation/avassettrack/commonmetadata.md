# commonMetadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of metadata items for all common metadata keys that have a value.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`commonMetadata`](../avpartialasyncproperty/commonmetadata-73m58.md) asynchronously instead.

## Declaration

```swift
var commonMetadata: [AVMetadataItem] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVMetadataItem *> * commonMetadata;
```

## See Also

### Accessing metadata
- [metadata](./metadata.md)
  An array of metadata items for all metadata identifiers that have a value.
- [availableMetadataFormats](./availablemetadataformats.md)
  An array of metadata formats available for the track.
- [- metadataForFormat:](./metadata%28forformat%29.md)
  Returns metadata items that a track contains for the specified format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/commonmetadata)*