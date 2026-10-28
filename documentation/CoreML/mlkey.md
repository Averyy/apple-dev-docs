# MLKey

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

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

```objc
@interface MLKey : NSObject
```

## Overview

You don’t create use this class directly. Instead, use a class that inherits from this one, such as [`MLParameterKey`](./mlparameterkey.md) or [`MLMetricKey`](./mlmetrickey.md).

## Topics

### Retrieving a key’s information
- [var name: String](./mlkey/name.md)
  The name of the machine learning key.
- [var scope: String?](./mlkey/scope.md)
  The applicable scope of the machine learning key.
### Initializers
- [init?(coder: NSCoder)](./mlkey/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MLMetricKey](./mlmetrickey.md)
- [MLParameterKey](./mlparameterkey.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Supporting types
- [class MLModelConfiguration](./mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.
- [struct MLOptimizationHints](./mloptimizationhints-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlkey)*