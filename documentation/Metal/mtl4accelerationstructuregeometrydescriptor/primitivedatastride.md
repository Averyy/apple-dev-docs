# primitiveDataStride

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Defines the stride, in bytes, between each primitive’s data in the primitive data buffer [`primitiveDataBuffer`](./primitivedatabuffer.md) references.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var primitiveDataStride: Int { get set }
```

```objc
@property (nonatomic) NSUInteger primitiveDataStride;
```

## Discussion

You are responsible for ensuring the stride is at least [`primitiveDataElementSize`](./primitivedataelementsize.md) in size and a multiple of 4 bytes.

This property defaults to `0` bytes,  which indicates the stride is equal to [`primitiveDataElementSize`](./primitivedataelementsize.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedatastride)*