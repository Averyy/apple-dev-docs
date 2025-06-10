# tensorReferenceType()

**Framework**: Metal  
**Kind**: method

Provides a description of the underlying tensor type when this struct member holds a tensor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func tensorReferenceType() -> MTLTensorReferenceType?
```

#### Return Value

A description of the tensor type that this struct member holds, or `nil` if this struct member doesn’t hold a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember/tensorreferencetype())*