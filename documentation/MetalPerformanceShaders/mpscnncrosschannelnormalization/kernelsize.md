# kernelSize

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The size of the square kernel window.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var kernelSize: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger kernelSize;
```

#### Discussion

The default value is `5`.

## See Also

### Instance Properties
- [var alpha: Float](./alpha.md)
  The “alpha” variable of the kernel function.
- [var beta: Float](./beta.md)
  The “beta” variable of the kernel function.
- [var delta: Float](./delta.md)
  The “delta” variable of the kernel function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalization/kernelsize)*