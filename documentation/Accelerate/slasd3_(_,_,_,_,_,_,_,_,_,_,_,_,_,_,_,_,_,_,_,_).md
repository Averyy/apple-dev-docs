# slasd3_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func slasd3_(_ nl: UnsafePointer<__LAPACK_int>, _ nr: UnsafePointer<__LAPACK_int>, _ sqre: UnsafePointer<__LAPACK_int>, _ k: UnsafePointer<__LAPACK_int>, _ d: UnsafeMutablePointer<Float>?, _ q: UnsafeMutablePointer<Float>?, _ ldq: UnsafePointer<__LAPACK_int>, _ dsigma: UnsafeMutablePointer<Float>?, _ u: UnsafeMutablePointer<Float>?, _ ldu: UnsafePointer<__LAPACK_int>, _ u2: UnsafePointer<Float>?, _ ldu2: UnsafePointer<__LAPACK_int>, _ vt: UnsafeMutablePointer<Float>?, _ ldvt: UnsafePointer<__LAPACK_int>, _ vt2: UnsafeMutablePointer<Float>?, _ ldvt2: UnsafePointer<__LAPACK_int>, _ idxc: UnsafePointer<__LAPACK_int>?, _ ctot: UnsafePointer<__LAPACK_int>?, _ z: UnsafeMutablePointer<Float>?, _ info: UnsafeMutablePointer<__LAPACK_int>)
```

```c
void slasd3_(const __LAPACK_int *nl, const __LAPACK_int *nr, const __LAPACK_int *sqre, const __LAPACK_int *k, float *d, float *q, const __LAPACK_int *ldq, float *dsigma, float *u, const __LAPACK_int *ldu, const float *u2, const __LAPACK_int *ldu2, float *vt, const __LAPACK_int *ldvt, float *vt2, const __LAPACK_int *ldvt2, const __LAPACK_int *idxc, const __LAPACK_int *ctot, float *z, __LAPACK_int *info);
```

## See Also

### Functions
- [func caxpy_(UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./caxpy_%28_,_,_,_,_,_%29.md)
- [func ccopy_(UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./ccopy_%28_,_,_,_,_%29.md)
- [func cdotc_(OpaquePointer, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cdotc_%28_,_,_,_,_,_%29.md)
- [func cdotu_(OpaquePointer, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cdotu_%28_,_,_,_,_,_%29.md)
- [func cgbmv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cgbmv_%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func cgemm_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cgemm_%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func cgemv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cgemv_%28_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func cgerc_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cgerc_%28_,_,_,_,_,_,_,_,_%29.md)
- [func cgeru_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cgeru_%28_,_,_,_,_,_,_,_,_%29.md)
- [func chbmv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./chbmv_%28_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func chemm_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./chemm_%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func chemv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./chemv_%28_,_,_,_,_,_,_,_,_,_%29.md)
- [func cher2_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cher2_%28_,_,_,_,_,_,_,_,_%29.md)
- [func cher2k_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cher2k_%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func cher_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cher_%28_,_,_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/slasd3_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*