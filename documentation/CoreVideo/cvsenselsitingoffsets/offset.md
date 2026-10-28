# CVSenselSitingOffsets.Offset

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

Siting offset of a component, relative to pixel center.

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
struct Offset
```

## Overview

A positive offset value indicates that the sensel/component lies to the right of or below the center of its pixel, while a negative value indicates that the sensel/component lies to the left of or above the center of its pixel. Horizontal and vertical offset magnitudes are respectively in terms of the spacing between horizontally and vertically-adjacent pixel centers.

## Topics

### Initializers
- [init(horizontal: Float32, vertical: Float32)](./offset/init%28horizontal,vertical%29.md)
### Instance Properties
- [var horizontal: Float32](./offset/horizontal.md)
- [var vertical: Float32](./offset/vertical.md)
### Type Properties
- [static let zero: CVSenselSitingOffsets.Offset](./offset/zero.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvsenselsitingoffsets/offset)*