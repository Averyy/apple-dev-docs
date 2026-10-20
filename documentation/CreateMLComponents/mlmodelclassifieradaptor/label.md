# MLModelClassifierAdaptor.Label

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

The classifier label type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
enum Label
```

## Topics

### Label types
- [MLModelClassifierAdaptor.Label.int(_:)](./label/int%28_%29.md)
  The label is integer type.
- [MLModelClassifierAdaptor.Label.string(_:)](./label/string%28_%29.md)
  The label is string type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./label/customdebugstringconvertible-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./label/expressiblebyintegerliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](./label/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByIntegerLiteral](../../Swift/expressiblebyintegerliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Performing the transformation
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> ClassificationDistribution<MLModelClassifierAdaptor<Scalar>.Label>](./applied%28to,eventhandler%29.md)
  Performs a prediction from a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelclassifieradaptor/label)*