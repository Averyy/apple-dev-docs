# primitiveDataElementSize

**Framework**: Metal  
**Kind**: property

Sets the size, in bytes, of the data for each primitive in the primitive data buffer [`primitiveDataBuffer`](mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer.md) references.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var primitiveDataElementSize: Int { get set }
```

#### Discussion

This size needs to be at most [`primitiveDataStride`](mtl4accelerationstructuregeometrydescriptor/primitivedatastride.md) in size and a multiple of 4 bytes.

This property defaults to 0 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedataelementsize)*