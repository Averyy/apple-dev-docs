# MPSCNNDropoutGradientState

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A class that stores the mask used by dropout and gradient dropout filters.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDropoutGradientState
```

```objc
@interface MPSCNNDropoutGradientState : MPSNNGradientState
```

## Topics

### Instance Methods
- [func maskData() -> Data](./mpscnndropoutgradientstate/maskdata%28%29.md)

## Relationships

### Inherits From
- [MPSNNGradientState](./mpsnngradientstate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Dropout Layers
- [class MPSCNNDropout](./mpscnndropout.md)
  A dropout filter.
- [class MPSCNNDropoutGradient](./mpscnndropoutgradient.md)
  A gradient dropout filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropoutgradientstate)*