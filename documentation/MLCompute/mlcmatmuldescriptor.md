# MLCMatMulDescriptor

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A configuration object you use to create a matrix multiplication layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCMatMulDescriptor
```

```objc
@interface MLCMatMulDescriptor : NSObject
```

## Topics

### Creating Matrix Multiplication Descriptors
- [convenience init()](./mlcmatmuldescriptor/init%28%29.md)
  Creates a batched matrix multiplication descriptor.
- [convenience init?(alpha: Float, transposesX: Bool, transposesY: Bool)](./mlcmatmuldescriptor/init%28alpha,transposesx,transposesy%29.md)
  Creates a batched matrix multiplication descriptor with the alpha value and transpose options you specify.
### Inspecting Matrix Multiplication Descriptors
- [var alpha: Float](./mlcmatmuldescriptor/alpha.md)
  A scalar value you specify to scale the result in C = alpha x A x B.
- [var transposesX: Bool](./mlcmatmuldescriptor/transposesx.md)
  A Boolean that specifies whether you choose to transpose the last two dimensions of x.
- [var transposesY: Bool](./mlcmatmuldescriptor/transposesy.md)
  A Boolean that specifies whether you choose to transpose the last two dimensions of y.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating Matrix Multiplication Layers
- [convenience init?(descriptor: MLCMatMulDescriptor)](./mlcmatmullayer/init%28descriptor%29.md)
  Creates a matrix multiplication layer with the specified descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmatmuldescriptor)*