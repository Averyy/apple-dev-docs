# makeDepthStencilState(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a depth-stencil state instance.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeDepthStencilState(descriptor: MTLDepthStencilDescriptor) -> (any MTLDepthStencilState)?
```

#### Return Value

A new [`MTLDepthStencilState`](mtldepthstencilstate.md) instance if the method completed successfully; otherwise `nil`.

## Parameters

- `descriptor`: An   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makedepthstencilstate(descriptor:))*