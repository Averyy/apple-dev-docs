# MLCPlatform

**Framework**: ML Compute  
**Kind**: class

A utility class for setting global properties in the framework.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
class MLCPlatform
```

## Topics

### Getting the RNG Seed
- [class func getRNGseed() -> NSNumber?](mlcplatform/getrngseed.md)
  Returns the global random number generator seed value.
### Setting the RNG Seed
- [class func setRNGSeedTo(NSNumber)](mlcplatform/setrngseedto(_:).md)
  Sets the global random number generator seed value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCTensor](mlctensor.md)
  The data object you use throughout the framework.
- [Layers](layers.md)
  Create and inspect layers that encapsulate operations and configuration details to receive, process, and output tensors.
- [Training and Validation](training-and-validation.md)
  Create, train, and validate a graph to produce acceptable prediction results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcplatform)*