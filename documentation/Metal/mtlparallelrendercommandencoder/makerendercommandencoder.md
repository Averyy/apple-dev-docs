# makeRenderCommandEncoder()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Create an object that encodes commands that perform graphics rendering operations and may be assigned to a different thread.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeRenderCommandEncoder() -> (any MTLRenderCommandEncoder)?
```

#### Return Value

A graphics rendering command encoder object

#### Discussion

The rendering commands encoded by [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) objects are executed in the order in which the [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) objects are created, not in the order they are ended.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/makerendercommandencoder())*