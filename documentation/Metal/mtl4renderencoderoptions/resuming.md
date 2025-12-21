# resuming

**Framework**: Metal  
**Kind**: property

Configures the render pass to as .

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var resuming: MTL4RenderEncoderOptions { get }
```

#### Discussion

Pass this option to [`makeRenderCommandEncoder(descriptor:options:)`](mtl4commandbuffer/makerendercommandencoder(descriptor:options:).md) to specify that Metal can stitch the work a render command encoder encodes with a prior “suspending” render command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderencoderoptions/resuming)*