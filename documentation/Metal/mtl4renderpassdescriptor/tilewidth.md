# tileWidth

**Framework**: Metal  
**Kind**: property

Sets the width, in pixels, of the tiles into which Metal divides the render attachments for tile-based rendering.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var tileWidth: Int { get set }
```

#### Discussion

When set to `0`, the default, Metal chooses a width that fits within local memory.

See also: doc:tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering.md


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/tilewidth)*