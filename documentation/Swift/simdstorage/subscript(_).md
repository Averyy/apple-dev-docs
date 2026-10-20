# subscript(_:)

**Framework**: Swift  
**Kind**: subscript  
**Role**: Instance Subscript  
**Required**: Yes

Accesses the element at the specified index.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
subscript(index: Int) -> Self.Scalar { get set }
```

## Parameters

- `index`: The index of the element to access. `index` must be in the range `0..<scalarCount`.

## Default Implementations

### SIMDStorage Implementations
- [subscript<Index>(SIMD2<Index>) -> SIMD2<Self.Scalar>](./subscript%28_%29-11tl0.md)
  Extracts the scalars at specified indices to form a SIMD2.
- [subscript<Index>(SIMD64<Index>) -> SIMD64<Self.Scalar>](./subscript%28_%29-4bxif.md)
  Extracts the scalars at specified indices to form a SIMD64.
- [subscript<Index>(SIMD4<Index>) -> SIMD4<Self.Scalar>](./subscript%28_%29-4wdyq.md)
  Extracts the scalars at specified indices to form a SIMD4.
- [subscript<Index>(SIMD8<Index>) -> SIMD8<Self.Scalar>](./subscript%28_%29-5dslw.md)
  Extracts the scalars at specified indices to form a SIMD8.
- [subscript<Index>(SIMD16<Index>) -> SIMD16<Self.Scalar>](./subscript%28_%29-8lp1s.md)
  Extracts the scalars at specified indices to form a SIMD16.
- [subscript<Index>(SIMD32<Index>) -> SIMD32<Self.Scalar>](./subscript%28_%29-9go95.md)
  Extracts the scalars at specified indices to form a SIMD32.
- [subscript<Index>(SIMD3<Index>) -> SIMD3<Self.Scalar>](./subscript%28_%29-9ota9.md)
  Extracts the scalars at specified indices to form a SIMD3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdstorage/subscript(_:))*