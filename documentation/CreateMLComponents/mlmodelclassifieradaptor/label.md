# MLModelClassifierAdaptor.Label

**Framework**: Create ML Components  
**Kind**: enum

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
- [MLModelClassifierAdaptor.Label.int(_:)](mlmodelclassifieradaptor/label/int(_:).md)
  The label is integer type.
- [MLModelClassifierAdaptor.Label.string(_:)](mlmodelclassifieradaptor/label/string(_:).md)
  The label is string type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlmodelclassifieradaptor/label/customdebugstringconvertible-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](mlmodelclassifieradaptor/label/expressiblebyintegerliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](mlmodelclassifieradaptor/label/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> ClassificationDistribution<MLModelClassifierAdaptor<Scalar>.Label>](mlmodelclassifieradaptor/applied(to:eventhandler:).md)
  Performs a prediction from a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelclassifieradaptor/label)*