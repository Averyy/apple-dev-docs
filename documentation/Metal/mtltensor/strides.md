# strides

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

An array of strides, in elements, one for each dimension of this tensor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var strides: MTLTensorExtents? { get }
```

#### Discussion

This property only applies if this tensor shares its storage with a buffer, otherwise it’s nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/strides)*