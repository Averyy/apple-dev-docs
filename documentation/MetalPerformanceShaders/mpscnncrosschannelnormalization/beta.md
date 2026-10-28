# beta

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The “beta” variable of the kernel function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var beta: Float { get set }
```

```objc
@property (nonatomic, readwrite) float beta;
```

## Discussion

The default value is `5.0`.

## See Also

### Instance Properties
- [var alpha: Float](./alpha.md)
  The “alpha” variable of the kernel function.
- [var delta: Float](./delta.md)
  The “delta” variable of the kernel function.
- [var kernelSize: Int](./kernelsize.md)
  The size of the square kernel window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalization/beta)*