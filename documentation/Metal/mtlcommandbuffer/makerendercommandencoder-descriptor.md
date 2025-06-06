# makeRenderCommandEncoder(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a render command encoder from a descriptor.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> (any MTLRenderCommandEncoder)?
```

#### Discussion

Use an [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) instance’s methods to set up a single graphics-rendering pass.

## Parameters

- `renderPassDescriptor`: An   instance that configures the   the method returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makerendercommandencoder(descriptor:))*