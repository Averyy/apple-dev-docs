# backing

**Framework**: Core Video  
**Kind**: property

Defines how the memory for the pixel buffer backing is allocated. IOSurface backed pixel buffers can be shared between CPU and GPU also across process boundaries. Defaults to `Backing.ioSurface`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var backing: CVPixelBufferCreationAttributes.Backing
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffercreationattributes/backing-swift.property)*