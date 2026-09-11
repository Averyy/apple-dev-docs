# AVMetadataFocusTrackedObject

**Framework**: AVFoundation  
**Kind**: class

A metadata object that is maintained in focus by the camera’s auto focus system continuously tracking it.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
class AVMetadataFocusTrackedObject
```

#### Overview

[`AVMetadataFocusTrackedObject`](avmetadatafocustrackedobject.md) represents a single tracked object in a picture. It is an immutable object describing the focus-tracked object.

On supported platforms, [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md) outputs arrays of focus-tracked objects. See AVCaptureOutput.h.

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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatafocustrackedobject)*