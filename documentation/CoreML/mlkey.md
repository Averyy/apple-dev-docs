# MLKey

**Framework**: Core ML  
**Kind**: class

An abstract base class for machine learning key types.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class MLKey
```

#### Overview

You don’t create use this class directly. Instead, use a class that inherits from this one, such as [`MLParameterKey`](mlparameterkey.md) or [`MLMetricKey`](mlmetrickey.md).

## Topics

### Retrieving a key’s information
- [var name: String](mlkey/name.md)
  The name of the machine learning key.
- [var scope: String?](mlkey/scope.md)
  The applicable scope of the machine learning key.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MLMetricKey](mlmetrickey.md)
- [MLParameterKey](mlparameterkey.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MLModelConfiguration](mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.
- [struct MLOptimizationHints](mloptimizationhints-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlkey)*