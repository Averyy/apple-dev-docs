# vsignbitf(_:)

**Framework**: Accelerate  
**Kind**: func

For each vector element, returns a non-zero value if and only if the sign of `arg` is negative. This includes NaNs, infinities and zeros.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vsignbitf(_: vFloat) -> vUInt32
```

## See Also

- [func vclassifyf(vFloat) -> vUInt32](vclassifyf(_:).md)
  For each vector element, returns the class of the argument (one of the FP_ … constants defined in math.h).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsignbitf(_:))*