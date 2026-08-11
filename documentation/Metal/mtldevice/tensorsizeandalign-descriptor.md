# tensorSizeAndAlign(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Determines the size and alignment required to hold the data plane of a tensor you create with a descriptor in a buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func tensorSizeAndAlign(descriptor: MTLTensorDescriptor) -> MTLSizeAndAlign
```

#### Return Value

The size and alignment required to hold the data plane of a tensor you create with `descriptor` in a buffer.

#### Discussion

This method requires that `descriptor` does not configure any auxiliary planes.

## Parameters

- `descriptor`: The tensor descriptor configuring the data plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/tensorsizeandalign(descriptor:))*