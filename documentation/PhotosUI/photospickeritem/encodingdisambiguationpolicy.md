# PhotosPickerItem.EncodingDisambiguationPolicy

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

A type that determines the encoding to use when multiple encodings are available, based on the content type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct EncodingDisambiguationPolicy
```

## Topics

### Getting standard encoding policies
- [static let automatic: PhotosPickerItem.EncodingDisambiguationPolicy](./encodingdisambiguationpolicy/automatic.md)
  An encoding policy that chooses the best encoding.
- [static let current: PhotosPickerItem.EncodingDisambiguationPolicy](./encodingdisambiguationpolicy/current.md)
  An encoding policy that chooses the current encoding to avoid transcoding, if possible.
- [static let compatible: PhotosPickerItem.EncodingDisambiguationPolicy](./encodingdisambiguationpolicy/compatible.md)
  An encoding policy that chooses the most compatible encoding even if transcoding is necessary.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/photospickeritem/encodingdisambiguationpolicy)*