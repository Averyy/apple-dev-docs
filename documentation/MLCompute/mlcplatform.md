# MLCPlatform

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A utility class for setting global properties in the framework.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCPlatform
```

```objc
@interface MLCPlatform : NSObject
```

## Topics

### Getting the RNG Seed
- [class func getRNGseed() -> NSNumber?](./mlcplatform/getrngseed%28%29.md)
  Returns the global random number generator seed value.
### Setting the RNG Seed
- [class func setRNGSeedTo(NSNumber)](./mlcplatform/setrngseedto%28_%29.md)
  Sets the global random number generator seed value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Components
- [class MLCTensor](./mlctensor.md)
  The data object you use throughout the framework.
- [Layers](./layers.md)
  Create and inspect layers that encapsulate operations and configuration details to receive, process, and output tensors.
- [Training and Validation](./training-and-validation.md)
  Create, train, and validate a graph to produce acceptable prediction results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcplatform)*