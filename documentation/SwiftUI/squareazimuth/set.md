# SquareAzimuth.Set

**Framework**: SwiftUI  
**Kind**: struct

A set of horizontal directions that specify how someone can look at a volume.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@frozen
struct Set
```

#### Overview

Combine the [`SquareAzimuth`](squareazimuth.md) constants to name several directions at once. Pass a set to [`supportedVolumeViewpoints(_:)`](view/supportedvolumeviewpoints(_:).md) to say which sides the window bar and ornaments of a volume should follow someone to.

```swift
VolumeContentView()
    .supportedVolumeViewpoints([.front, .left])
```

A volume supports [`all`](squareazimuth/set/all.md) unless you narrow it. Narrow the set when your content only makes sense from certain sides, such as a model with a defined back that you never want someone to see the controls through.

## Topics

### Initializers
- [init(SquareAzimuth)](squareazimuth/set/init(_:).md)
  Creates a set containing only the specified [`SquareAzimuth`](squareazimuth.md).
### Instance Methods
- [func contains(SquareAzimuth) -> Bool](squareazimuth/set/contains(_:).md)
  Returns a Boolean value that indicates whether the set contains the specified [`SquareAzimuth`](squareazimuth.md).
### Type Properties
- [static let all: SquareAzimuth.Set](squareazimuth/set/all.md)
  A set containing all four of the [`SquareAzimuth`](squareazimuth.md) constants.
- [static let back: SquareAzimuth.Set](squareazimuth/set/back.md)
  A set containing only [`SquareAzimuth.back`](squareazimuth/back.md).
- [static let front: SquareAzimuth.Set](squareazimuth/set/front.md)
  A set containing only [`SquareAzimuth.front`](squareazimuth/front.md).
- [static let left: SquareAzimuth.Set](squareazimuth/set/left.md)
  A set containing only [`SquareAzimuth.left`](squareazimuth/left.md).
- [static let right: SquareAzimuth.Set](squareazimuth/set/right.md)
  A set containing only [`SquareAzimuth.right`](squareazimuth/right.md).

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/squareazimuth/set)*