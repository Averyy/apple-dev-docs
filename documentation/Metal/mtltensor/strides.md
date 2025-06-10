# strides

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

An array of strides, in elements, one for each dimension of this tensor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var strides: MTLTensorExtents { get }
```

#### Discussion

This property only applies if this tensor shares its storage with a buffer, otherwise it’s nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/strides)*