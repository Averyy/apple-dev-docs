# MLMetricKey

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

A key for the metrics dictionary in an update context.

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
class MLMetricKey
```

```objc
@interface MLMetricKey : MLKey
```

## Topics

### Getting the keys
- [class var lossValue: MLMetricKey](./mlmetrickey/lossvalue.md)
  The key you use to access the current loss (a `float` value).
- [class var epochIndex: MLMetricKey](./mlmetrickey/epochindex.md)
  The key you use to access the epoch index (an `Int64` value).
- [class var miniBatchIndex: MLMetricKey](./mlmetrickey/minibatchindex.md)
  The key you use to access the mini-batch index (an `Int64` value) within an epoch.
### Supporting types
- [class MLKey](./mlkey.md)
  An abstract base class for machine learning key types.

## Relationships

### Inherits From
- [MLKey](./mlkey.md)
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

### Evaluating the update
- [var metrics: [MLMetricKey : Any]](./mlupdatecontext/metrics.md)
  The training metrics of the model for the update task, contained in a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmetrickey)*