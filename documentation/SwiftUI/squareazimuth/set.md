# SquareAzimuth.Set

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A set of horizontal directions that specify how someone can look at a volume.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@frozen
struct Set
```

## Overview

Combine the [`SquareAzimuth`](../squareazimuth.md) constants to name several directions at once. Pass a set to [`supportedVolumeViewpoints(_:)`](../view/supportedvolumeviewpoints%28_%29.md) to say which sides the window bar and ornaments of a volume should follow someone to.

```swift
VolumeContentView()
    .supportedVolumeViewpoints([.front, .left])
```

A volume supports [`all`](./set/all.md) unless you narrow it. Narrow the set when your content only makes sense from certain sides, such as a model with a defined back that you never want someone to see the controls through.

## Topics

### Initializers
- [init(SquareAzimuth)](./set/init%28_%29.md)
  Creates a set containing only the specified [`SquareAzimuth`](../squareazimuth.md).
### Instance Methods
- [func contains(SquareAzimuth) -> Bool](./set/contains%28_%29.md)
  Returns a Boolean value that indicates whether the set contains the specified [`SquareAzimuth`](../squareazimuth.md).
### Type Properties
- [static let all: SquareAzimuth.Set](./set/all.md)
  A set containing all four of the [`SquareAzimuth`](../squareazimuth.md) constants.
- [static let back: SquareAzimuth.Set](./set/back.md)
  A set containing only [`SquareAzimuth.back`](./back.md).
- [static let front: SquareAzimuth.Set](./set/front.md)
  A set containing only [`SquareAzimuth.front`](./front.md).
- [static let left: SquareAzimuth.Set](./set/left.md)
  A set containing only [`SquareAzimuth.left`](./left.md).
- [static let right: SquareAzimuth.Set](./set/right.md)
  A set containing only [`SquareAzimuth.right`](./right.md).

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/squareazimuth/set)*