# subscript(_:)

**Framework**: Metal  
**Kind**: subscript

Returns the state of the specified vertex buffer layout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
subscript(index: Int) -> MTLVertexBufferLayoutDescriptor! { get set }
```

#### Return Value

A descriptor that contains vertex buffer layout state.

## Parameters

- `index`: A specified index in the array of vertex buffer layouts.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray/subscript(_:))*