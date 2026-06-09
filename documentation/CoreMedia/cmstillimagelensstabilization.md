# CMStillImageLensStabilization

**Framework**: Core Media  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum CMStillImageLensStabilization
```

## Topics

### Enumeration Cases
- [CMStillImageLensStabilization.active](cmstillimagelensstabilization/active.md)
  The lens stabilization module was active for the duration this buffer.
- [CMStillImageLensStabilization.off](cmstillimagelensstabilization/off.md)
  The lens stabilization module was not used during this capture.
- [CMStillImageLensStabilization.outOfRange](cmstillimagelensstabilization/outofrange.md)
  The motion of the device or duration of the capture was outside of what the stabilization mechanism could support.
- [CMStillImageLensStabilization.unavailable](cmstillimagelensstabilization/unavailable.md)
  The lens stabilization module was unavailable for use.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](../CoreVideo/CVAttachmentValueRepresentable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmstillimagelensstabilization)*