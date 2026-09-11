# AVMetadataCinematicVideoMetadataObject

**Framework**: AVFoundation  
**Kind**: class

A metadata object containing opaque Cinematic video metadata for Cinematic video editing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
class AVMetadataCinematicVideoMetadataObject
```

#### Overview

This object represents Cinematic video metadata captured during a recording session using [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md).

## Topics

### Instance Properties
- [var timedMetadataGroup: AVTimedMetadataGroup?](avmetadatacinematicvideometadataobject/timedmetadatagroup.md)
  A timed metadata group containing the Cinematic video metadata.
### Type Properties
- [class var cinematicVideoMetadataFormatDescription: CMFormatDescription?](avmetadatacinematicvideometadataobject/cinematicvideometadataformatdescription.md)
  The format description for Cinematic video timed metadata sample buffers.

## Relationships

### Inherits From
- [AVMetadataObject](avmetadataobject.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatacinematicvideometadataobject)*