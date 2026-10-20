# slaqz3_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func slaqz3_(_ ilschur: UnsafePointer<__LAPACK_bool>, _ ilq: UnsafePointer<__LAPACK_bool>, _ ilz: UnsafePointer<__LAPACK_bool>, _ n: UnsafePointer<__LAPACK_int>, _ ilo: UnsafePointer<__LAPACK_int>, _ ihi: UnsafePointer<__LAPACK_int>, _ nw: UnsafePointer<__LAPACK_int>, _ a: UnsafeMutablePointer<Float>?, _ lda: UnsafePointer<__LAPACK_int>, _ b: UnsafeMutablePointer<Float>?, _ ldb: UnsafePointer<__LAPACK_int>, _ q: UnsafeMutablePointer<Float>?, _ ldq: UnsafePointer<__LAPACK_int>, _ z: UnsafeMutablePointer<Float>?, _ ldz: UnsafePointer<__LAPACK_int>, _ ns: UnsafeMutablePointer<__LAPACK_int>, _ nd: UnsafeMutablePointer<__LAPACK_int>, _ alphar: UnsafeMutablePointer<Float>?, _ alphai: UnsafeMutablePointer<Float>?, _ beta: UnsafeMutablePointer<Float>?, _ qc: UnsafeMutablePointer<Float>?, _ ldqc: UnsafePointer<__LAPACK_int>, _ zc: UnsafeMutablePointer<Float>?, _ ldzc: UnsafePointer<__LAPACK_int>, _ work: UnsafeMutablePointer<Float>, _ lwork: UnsafePointer<__LAPACK_int>, _ rec: UnsafePointer<__LAPACK_int>, _ info: UnsafeMutablePointer<__LAPACK_int>)
```

```c
void slaqz3_(const __LAPACK_bool *ilschur, const __LAPACK_bool *ilq, const __LAPACK_bool *ilz, const __LAPACK_int *n, const __LAPACK_int *ilo, const __LAPACK_int *ihi, const __LAPACK_int *nw, float *a, const __LAPACK_int *lda, float *b, const __LAPACK_int *ldb, float *q, const __LAPACK_int *ldq, float *z, const __LAPACK_int *ldz, __LAPACK_int *ns, __LAPACK_int *nd, float *alphar, float *alphai, float *beta, float *qc, const __LAPACK_int *ldqc, float *zc, const __LAPACK_int *ldzc, float *work, const __LAPACK_int *lwork, const __LAPACK_int *rec, __LAPACK_int *info);
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/slaqz3_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*