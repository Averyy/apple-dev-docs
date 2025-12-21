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
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> ClassificationDistribution<MLModelClassifierAdaptor<Scalar>.Label>](mlmodelclassifieradaptor/applied(to:eventhandler:).md)
  Performs a prediction from a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelclassifieradaptor/label)*