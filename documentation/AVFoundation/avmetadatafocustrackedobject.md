# AVMetadataFocusTrackedObject

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVMetadataFocusTrackedObject : AVMetadataObject
```

#### Overview

[`AVMetadataFocusTrackedObject`](./avmetadatafocustrackedobject.md) represents a single tracked object in a picture. It is an immutable object describing the focus-tracked object.

On supported platforms, [`AVCaptureMetadataOutput`](./avcapturemetadataoutput.md) outputs arrays of focus-tracked objects. See AVCaptureOutput.h.

## Relationships

### Inherits From
- [AVMetadataObject](./avmetadataobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatafocustrackedobject)*