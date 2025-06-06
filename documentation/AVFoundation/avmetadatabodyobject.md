# AVMetadataBodyObject

**Framework**: AVFoundation  
**Kind**: class

An abstract class that defines the interface for a metadata body object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
class AVMetadataBodyObject
```

#### Overview

A metadata body object represents a single detected body in a picture. It’s the base object used to represent bodies, for example [`AVMetadataHumanBodyObject`](avmetadatahumanbodyobject.md), [`AVMetadataDogBodyObject`](avmetadatadogbodyobject.md), and [`AVMetadataCatBodyObject`](avmetadatacatbodyobject.md).

## Topics

### Inspecting Metadata
- [var bodyID: Int](avmetadatabodyobject/bodyid.md)
  An integer value that defines the unique identifier of an object in a picture.

## Relationships

### Inherits From
- [AVMetadataObject](avmetadataobject.md)
### Inherited By
- [AVMetadataCatBodyObject](avmetadatacatbodyobject.md)
- [AVMetadataDogBodyObject](avmetadatadogbodyobject.md)
- [AVMetadataHumanBodyObject](avmetadatahumanbodyobject.md)
- [AVMetadataHumanFullBodyObject](avmetadatahumanfullbodyobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVMetadataCatBodyObject](avmetadatacatbodyobject.md)
  An object representing a single detected cat body in a picture.
- [class AVMetadataDogBodyObject](avmetadatadogbodyobject.md)
  An object representing a single detected dog body in a picture.
- [class AVMetadataHumanBodyObject](avmetadatahumanbodyobject.md)
  An object representing a single detected human body in a picture.
- [class AVMetadataHumanFullBodyObject](avmetadatahumanfullbodyobject.md)
  An object that represents a detected human full body in a picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatabodyobject)*