# suspending

**Framework**: Metal  
**Kind**: property

Configures the render pass as .

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var suspending: MTL4RenderEncoderOptions { get }
```

#### Discussion

Pass this option to [`makeRenderCommandEncoder(descriptor:options:)`](mtl4commandbuffer/makerendercommandencoder(descriptor:options:).md) to specify that Metal can stitch the work a render command encoder encodes with a subsequent “resuming” render command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderencoderoptions/suspending)*