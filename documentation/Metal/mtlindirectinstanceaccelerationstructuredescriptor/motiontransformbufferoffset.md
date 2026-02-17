# motionTransformBufferOffset

**Framework**: Metal  
**Kind**: property

The offset, in bytes, to the descripton of the first motion transform.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var motionTransformBufferOffset: Int { get set }
```

#### Discussion

The offset needs to be a multiple of 64 bytes. Check the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectinstanceaccelerationstructuredescriptor/motiontransformbufferoffset)*