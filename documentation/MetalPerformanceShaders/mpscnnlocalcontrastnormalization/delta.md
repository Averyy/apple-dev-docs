# delta

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The “delta” variable of the kernel function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var delta: Float { get set }
```

```objc
@property (nonatomic, readwrite) float delta;
```

#### Discussion

The default value is `1/1024`.

## See Also

### Instance Properties
- [var alpha: Float](./alpha.md)
  The “alpha” variable of the kernel function.
- [var beta: Float](./beta.md)
  The “beta” variable of the kernel function.
- [var p0: Float](./p0.md)
  The “p0” variable of the kernel function.
- [var pm: Float](./pm.md)
  The “pm” variable of the kernel function.
- [var ps: Float](./ps.md)
  The “ps” variable of the kernel function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalization/delta)*