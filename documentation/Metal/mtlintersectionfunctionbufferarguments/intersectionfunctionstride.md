# intersectionFunctionStride

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var intersectionFunctionStride: UInt64
```

```c
uint64_t intersectionFunctionStride;
```

#### Discussion

The stride between intersection function entries in intersectionFunctionBuffer. The stride needs to be either 0 or aligned to 8 bytes. Note that only the first 12 bits of this value are used by Metal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctionbufferarguments/intersectionfunctionstride)*