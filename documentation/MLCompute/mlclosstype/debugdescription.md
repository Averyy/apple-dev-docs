# debugDescription

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A textual description of the loss type, suitable for debugging.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var debugDescription: String { get }
```

```c
NSString *MLCLossTypeDebugDescription(MLCLossType lossType);
```

## See Also

### Enumeration Cases
- [MLCLossType.categoricalCrossEntropy](./categoricalcrossentropy.md)
- [MLCLossType.cosineDistance](./cosinedistance.md)
- [MLCLossType.hinge](./hinge.md)
- [MLCLossType.huber](./huber.md)
- [MLCLossType.log](./log.md)
- [MLCLossType.meanAbsoluteError](./meanabsoluteerror.md)
- [MLCLossType.meanSquaredError](./meansquarederror.md)
- [MLCLossType.sigmoidCrossEntropy](./sigmoidcrossentropy.md)
- [MLCLossType.softmaxCrossEntropy](./softmaxcrossentropy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclosstype/debugdescription)*