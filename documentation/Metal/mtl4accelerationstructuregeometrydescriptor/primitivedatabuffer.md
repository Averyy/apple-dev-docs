# primitiveDataBuffer

**Framework**: Metal  
**Kind**: property

Assigns optional buffer containing data to associate with each primitive in this geometry.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var primitiveDataBuffer: MTL4BufferRange { get set }
```

#### Discussion

You can use zero as the buffer address in this buffer range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer)*