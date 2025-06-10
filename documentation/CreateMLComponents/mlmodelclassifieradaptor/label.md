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
### Operators
- [static func == (MLModelClassifierAdaptor<Scalar>.Label, MLModelClassifierAdaptor<Scalar>.Label) -> Bool](mlmodelclassifieradaptor/label/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mlmodelclassifieradaptor/label/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mlmodelclassifieradaptor/label/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlmodelclassifieradaptor/label/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](mlmodelclassifieradaptor/label/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](mlmodelclassifieradaptor/label/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](mlmodelclassifieradaptor/label/expressiblebyintegerliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](mlmodelclassifieradaptor/label/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](mlmodelclassifieradaptor/label/expressiblebyunicodescalarliteral-implementations.md)

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