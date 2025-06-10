# dlarrv_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

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
func dlarrv_(_ n: UnsafePointer<__LAPACK_int>, _ vl: UnsafePointer<Double>, _ vu: UnsafePointer<Double>, _ d: UnsafeMutablePointer<Double>?, _ l: UnsafeMutablePointer<Double>?, _ pivmin: UnsafePointer<Double>, _ isplit: UnsafePointer<__LAPACK_int>?, _ m: UnsafePointer<__LAPACK_int>, _ dol: UnsafePointer<__LAPACK_int>, _ dou: UnsafePointer<__LAPACK_int>, _ minrgp: UnsafePointer<Double>, _ rtol1: UnsafeMutablePointer<Double>, _ rtol2: UnsafeMutablePointer<Double>, _ w: UnsafeMutablePointer<Double>?, _ werr: UnsafeMutablePointer<Double>?, _ wgap: UnsafeMutablePointer<Double>?, _ iblock: UnsafePointer<__LAPACK_int>?, _ indexw: UnsafePointer<__LAPACK_int>?, _ gers: UnsafePointer<Double>?, _ z: UnsafeMutablePointer<Double>?, _ ldz: UnsafePointer<__LAPACK_int>, _ isuppz: UnsafeMutablePointer<__LAPACK_int>?, _ work: UnsafeMutablePointer<Double>, _ iwork: UnsafeMutablePointer<__LAPACK_int>?, _ info: UnsafeMutablePointer<__LAPACK_int>)
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/dlarrv_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*