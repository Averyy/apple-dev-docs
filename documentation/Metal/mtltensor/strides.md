# strides

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An array of strides, in elements, one for each dimension of this tensor, if applicable.

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

```objc
@property (readonly, nullable) MTLTensorExtents * strides;
```

#### Discussion

This property is non-nil only for tensors created from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/strides)*