# cleanRect

**Framework**: Core Video  
**Kind**: property

Source rectangle of a CVImageBuffer that represents the clean aperture of the buffer in encoded pixels. For example, an NTSC DV frame would return a CGRect with an origin of 8,0 and a size of 704,480. Note that the origin of this rect always the lower left corner. This is the same coordinate system as used by CoreImage.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var cleanRect: CGRect { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferrepresentable/cleanrect)*