# primitiveDataBuffer

**Framework**: Metal  
**Kind**: property

Assigns optional buffer containing data to associate with each primitive in this geometry.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var primitiveDataBuffer: MTL4BufferRange { get set }
```

#### Discussion

You can use zero as the buffer address in this buffer range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer)*