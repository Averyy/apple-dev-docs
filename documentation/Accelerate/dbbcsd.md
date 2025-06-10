# dbbcsd_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

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
func dbbcsd_(_ jobu1: UnsafePointer<CChar>, _ jobu2: UnsafePointer<CChar>, _ jobv1t: UnsafePointer<CChar>, _ jobv2t: UnsafePointer<CChar>, _ trans: UnsafePointer<CChar>, _ m: UnsafePointer<__LAPACK_int>, _ p: UnsafePointer<__LAPACK_int>, _ q: UnsafePointer<__LAPACK_int>, _ theta: UnsafeMutablePointer<Double>?, _ phi: UnsafeMutablePointer<Double>?, _ u1: UnsafeMutablePointer<Double>?, _ ldu1: UnsafePointer<__LAPACK_int>, _ u2: UnsafeMutablePointer<Double>?, _ ldu2: UnsafePointer<__LAPACK_int>, _ v1t: UnsafeMutablePointer<Double>?, _ ldv1t: UnsafePointer<__LAPACK_int>, _ v2t: UnsafeMutablePointer<Double>?, _ ldv2t: UnsafePointer<__LAPACK_int>, _ b11d: UnsafeMutablePointer<Double>?, _ b11e: UnsafeMutablePointer<Double>?, _ b12d: UnsafeMutablePointer<Double>?, _ b12e: UnsafeMutablePointer<Double>?, _ b21d: UnsafeMutablePointer<Double>?, _ b21e: UnsafeMutablePointer<Double>?, _ b22d: UnsafeMutablePointer<Double>?, _ b22e: UnsafeMutablePointer<Double>?, _ work: UnsafeMutablePointer<Double>, _ lwork: UnsafePointer<__LAPACK_int>, _ info: UnsafeMutablePointer<__LAPACK_int>)
```

## See Also

- [func caxpy_(UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](caxpy_(_:_:_:_:_:_:).md)
- [func ccopy_(UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](ccopy_(_:_:_:_:_:).md)
- [func cdotc_(OpaquePointer, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cdotc_(_:_:_:_:_:_:).md)
- [func cdotu_(OpaquePointer, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cdotu_(_:_:_:_:_:_:).md)
- [func cgbmv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cgbmv_(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cgemm_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cgemm_(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cgemv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cgemv_(_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cgerc_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cgerc_(_:_:_:_:_:_:_:_:_:).md)
- [func cgeru_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cgeru_(_:_:_:_:_:_:_:_:_:).md)
- [func chbmv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](chbmv_(_:_:_:_:_:_:_:_:_:_:_:).md)
- [func chemm_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](chemm_(_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func chemv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](chemv_(_:_:_:_:_:_:_:_:_:_:).md)
- [func cher2_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cher2_(_:_:_:_:_:_:_:_:_:).md)
- [func cher2k_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cher2k_(_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cher_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cher_(_:_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/dbbcsd_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*