# zlarf1f_(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func zlarf1f_(_ side: UnsafePointer<CChar>, _ m: UnsafePointer<__LAPACK_int>, _ n: UnsafePointer<__LAPACK_int>, _ v: OpaquePointer?, _ incv: UnsafePointer<__LAPACK_int>, _ tau: OpaquePointer, _ c: OpaquePointer?, _ ldc: UnsafePointer<__LAPACK_int>, _ work: OpaquePointer?)
```

```c
void zlarf1f_(const char *side, const __LAPACK_int *m, const __LAPACK_int *n, const __LAPACK_double_complex *v, const __LAPACK_int *incv, const __LAPACK_double_complex *tau, __LAPACK_double_complex *c, const __LAPACK_int *ldc, __LAPACK_double_complex *work);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/zlarf1f_(_:_:_:_:_:_:_:_:_:))*