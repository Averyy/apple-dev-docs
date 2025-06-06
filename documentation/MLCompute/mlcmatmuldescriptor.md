# MLCMatMulDescriptor

**Framework**: ML Compute  
**Kind**: class

A configuration object you use to create a matrix multiplication layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCMatMulDescriptor
```

## Topics

### Creating Matrix Multiplication Descriptors
- [convenience init()](mlcmatmuldescriptor/init.md)
  Creates a batched matrix multiplication descriptor.
- [convenience init?(alpha: Float, transposesX: Bool, transposesY: Bool)](mlcmatmuldescriptor/init(alpha:transposesx:transposesy:).md)
  Creates a batched matrix multiplication descriptor with the alpha value and transpose options you specify.
### Inspecting Matrix Multiplication Descriptors
- [var alpha: Float](mlcmatmuldescriptor/alpha.md)
  A scalar value you specify to scale the result in C = alpha x A x B.
- [var transposesX: Bool](mlcmatmuldescriptor/transposesx.md)
  A Boolean that specifies whether you choose to transpose the last two dimensions of x.
- [var transposesY: Bool](mlcmatmuldescriptor/transposesy.md)
  A Boolean that specifies whether you choose to transpose the last two dimensions of y.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init?(descriptor: MLCMatMulDescriptor)](mlcmatmullayer/init(descriptor:).md)
  Creates a matrix multiplication layer with the specified descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmatmuldescriptor)*