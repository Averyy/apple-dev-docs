# tensorSizeAndAlign(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Determines the size and alignment required to hold the data of a tensor you create with a descriptor in a buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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