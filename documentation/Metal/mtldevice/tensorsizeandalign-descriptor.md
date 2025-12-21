# tensorSizeAndAlign(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Determines the size and alignment required to hold the data of a tensor you create with a descriptor in a buffer.

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

The size and alignment required to hold the data of a tensor you create with `descriptor` in a buffer.

## Parameters

- `descriptor`: A description of the properties for the new tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/tensorsizeandalign(descriptor:))*