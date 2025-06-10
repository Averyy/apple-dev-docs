# dlaqz0_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

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
func dlaqz0_(_ wants: UnsafePointer<CChar>, _ wantq: UnsafePointer<CChar>, _ wantz: UnsafePointer<CChar>, _ n: UnsafePointer<__LAPACK_int>, _ ilo: UnsafePointer<__LAPACK_int>, _ ihi: UnsafePointer<__LAPACK_int>, _ a: UnsafeMutablePointer<Double>?, _ lda: UnsafePointer<__LAPACK_int>, _ b: UnsafeMutablePointer<Double>?, _ ldb: UnsafePointer<__LAPACK_int>, _ alphar: UnsafeMutablePointer<Double>?, _ alphai: UnsafeMutablePointer<Double>?, _ beta: UnsafeMutablePointer<Double>?, _ q: UnsafeMutablePointer<Double>?, _ ldq: UnsafePointer<__LAPACK_int>, _ z: UnsafeMutablePointer<Double>?, _ ldz: UnsafePointer<__LAPACK_int>, _ work: UnsafeMutablePointer<Double>, _ lwork: UnsafePointer<__LAPACK_int>, _ rec: UnsafePointer<__LAPACK_int>, _ info: UnsafeMutablePointer<__LAPACK_int>)
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/dlaqz0_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*