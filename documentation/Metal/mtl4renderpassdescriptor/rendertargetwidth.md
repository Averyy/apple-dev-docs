# renderTargetWidth

**Framework**: Metal  
**Kind**: property

Sets the width, in pixels, to which Metal constrains the render target.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var renderTargetWidth: Int { get set }
```

#### Discussion

When this value is non-zero, you need to assign it to be smaller than or equal to the minimum width of all attachments.

The default value of this property is `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/rendertargetwidth)*