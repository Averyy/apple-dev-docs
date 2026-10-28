# MTLMultisampleStencilResolveFilter.depthResolvedSample

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Chooses the stencil sample corresponding to the depth sample selected by the depth resolve filter.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
case depthResolvedSample
```

```c
MTLMultisampleStencilResolveFilterDepthResolvedSample
```

## Discussion

The resolve filter selects the stencil sample corresponding to the sample that the depth resolve filter would have selected.

## See Also

### Stencil resolve filters
- [MTLMultisampleStencilResolveFilter.sample0](./sample0.md)
  Chooses the first stencil sample in the pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmultisamplestencilresolvefilter/depthresolvedsample)*