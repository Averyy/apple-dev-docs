# vclassifyf(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

For each vector element, returns the class of the argument (one of the FP_ … constants defined in math.h).

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vclassifyf(_: vFloat) -> vUInt32
```

```c
extern vUInt32 vclassifyf(vFloat );
```

## See Also

### Inquiry Functions (from vfp.h)
- [func vsignbitf(vFloat) -> vUInt32](./vsignbitf%28_%29.md)
  For each vector element, returns a non-zero value if and only if the sign of `arg` is negative. This includes NaNs, infinities and zeros.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vclassifyf(_:))*