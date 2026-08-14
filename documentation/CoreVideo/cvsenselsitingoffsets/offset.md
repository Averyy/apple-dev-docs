# CVSenselSitingOffsets.Offset

**Framework**: Core Video  
**Kind**: struct

Siting offset of a component, relative to pixel center.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Offset
```

#### Overview

A positive offset value indicates that the sensel/component lies to the right of or below the center of its pixel, while a negative value indicates that the sensel/component lies to the left of or above the center of its pixel. Horizontal and vertical offset magnitudes are respectively in terms of the spacing between horizontally and vertically-adjacent pixel centers.

## Topics

### Initializers
- [init(horizontal: Float32, vertical: Float32)](cvsenselsitingoffsets/offset/init(horizontal:vertical:).md)
### Instance Properties
- [var horizontal: Float32](cvsenselsitingoffsets/offset/horizontal.md)
- [var vertical: Float32](cvsenselsitingoffsets/offset/vertical.md)
### Type Properties
- [static let zero: CVSenselSitingOffsets.Offset](cvsenselsitingoffsets/offset/zero.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvsenselsitingoffsets/offset)*