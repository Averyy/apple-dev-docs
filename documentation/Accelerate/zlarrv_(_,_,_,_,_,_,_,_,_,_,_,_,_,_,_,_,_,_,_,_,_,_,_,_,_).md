# zlarrv_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

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
func zlarrv_(_ n: UnsafePointer<__LAPACK_int>, _ vl: UnsafePointer<Double>, _ vu: UnsafePointer<Double>, _ d: UnsafeMutablePointer<Double>?, _ l: UnsafeMutablePointer<Double>?, _ pivmin: UnsafePointer<Double>, _ isplit: UnsafePointer<__LAPACK_int>?, _ m: UnsafePointer<__LAPACK_int>, _ dol: UnsafePointer<__LAPACK_int>, _ dou: UnsafePointer<__LAPACK_int>, _ minrgp: UnsafePointer<Double>, _ rtol1: UnsafeMutablePointer<Double>, _ rtol2: UnsafeMutablePointer<Double>, _ w: UnsafeMutablePointer<Double>?, _ werr: UnsafeMutablePointer<Double>?, _ wgap: UnsafeMutablePointer<Double>?, _ iblock: UnsafePointer<__LAPACK_int>?, _ indexw: UnsafePointer<__LAPACK_int>?, _ gers: UnsafePointer<Double>?, _ z: OpaquePointer?, _ ldz: UnsafePointer<__LAPACK_int>, _ isuppz: UnsafeMutablePointer<__LAPACK_int>?, _ work: UnsafeMutablePointer<Double>, _ iwork: UnsafeMutablePointer<__LAPACK_int>?, _ info: UnsafeMutablePointer<__LAPACK_int>)
```

```c
void zlarrv_(const __LAPACK_int *n, const double *vl, const double *vu, double *d, double *l, const double *pivmin, const __LAPACK_int *isplit, const __LAPACK_int *m, const __LAPACK_int *dol, const __LAPACK_int *dou, const double *minrgp, double *rtol1, double *rtol2, double *w, double *werr, double *wgap, const __LAPACK_int *iblock, const __LAPACK_int *indexw, const double *gers, __LAPACK_double_complex *z, const __LAPACK_int *ldz, __LAPACK_int *isuppz, double *work, __LAPACK_int *iwork, __LAPACK_int *info);
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/zlarrv_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*