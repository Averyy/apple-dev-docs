# MLOptimizationHints

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

MLOptimizationHints

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```objc
@interface MLOptimizationHints : NSObject
```

## Overview

An object to hold hints that CoreML could use for further optimization

## Topics

### Getting the reshape frequency
- [reshapeFrequency](./mloptimizationhints-c.class/reshapefrequency.md)
  The anticipated reshape frequency
### Getting the specialization strategy
- [specializationStrategy](./mloptimizationhints-c.class/specializationstrategy.md)
  Optimization strategy for the model specialization.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Optimization
- [Analyzing a Core ML model’s performance in Xcode](./analyzing-a-core-ml-model-s-performance-in-xcode.md)
  Measure how your model runs on your Mac or a connected device by generating a performance report in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mloptimizationhints-c.class)*