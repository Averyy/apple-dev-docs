# renderTargetWidth

**Framework**: Metal  
**Kind**: property

Sets the width, in pixels, to which Metal constrains the render target.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var renderTargetWidth: Int { get set }
```

#### Discussion

When this value is non-zero, you need to assign it to be smaller than or equal to the minimum width of all attachments.

The default value of this property is `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/rendertargetwidth)*