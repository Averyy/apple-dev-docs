# CMStillImageLensStabilization

**Framework**: Core Media  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum CMStillImageLensStabilization
```

## Topics

### Enumeration Cases
- [CMStillImageLensStabilization.active](./cmstillimagelensstabilization/active.md)
  The lens stabilization module was active for the duration this buffer.
- [CMStillImageLensStabilization.off](./cmstillimagelensstabilization/off.md)
  The lens stabilization module was not used during this capture.
- [CMStillImageLensStabilization.outOfRange](./cmstillimagelensstabilization/outofrange.md)
  The motion of the device or duration of the capture was outside of what the stabilization mechanism could support.
- [CMStillImageLensStabilization.unavailable](./cmstillimagelensstabilization/unavailable.md)
  The lens stabilization module was unavailable for use.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](../CoreVideo/cvattachmentvaluerepresentable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmstillimagelensstabilization)*