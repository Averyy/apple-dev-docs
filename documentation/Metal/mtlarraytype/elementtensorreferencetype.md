# elementTensorReferenceType()

**Framework**: Metal  
**Kind**: method

Provides a description of the underlying tensor type when this array holds tensors as its elements.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func elementTensorReferenceType() -> MTLTensorReferenceType?
```

#### Return Value

A description of the tensor type that this array holds, or `nil` if this struct member doesn’t hold a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlarraytype/elementtensorreferencetype())*