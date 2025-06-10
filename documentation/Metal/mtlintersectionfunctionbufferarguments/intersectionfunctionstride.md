# intersectionFunctionStride

**Framework**: Metal  
**Kind**: property

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var intersectionFunctionStride: UInt64
```

#### Discussion

The stride needs to be either 0 or aligned to 8 bytes. Note that only the first 12 bits of this value are used by Metal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctionbufferarguments/intersectionfunctionstride)*