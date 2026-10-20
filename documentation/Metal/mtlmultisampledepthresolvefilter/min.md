# MTLMultisampleDepthResolveFilter.min

**Framework**: Metal  
**Kind**: case  
**Role**: Case

The GPU compares all depth samples in the pixel and selects the sample with the smallest value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case min
```

```c
MTLMultisampleDepthResolveFilterMin
```

## See Also

### Depth resolve filters
- [MTLMultisampleDepthResolveFilter.sample0](./sample0.md)
  No filter is applied.
- [MTLMultisampleDepthResolveFilter.max](./max.md)
  The GPU compares all depth samples in the pixel and selects the sample with the largest value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter/min)*