# depthResolveFilter

**Framework**: Metal  
**Kind**: property

The filter used for an MSAA depth resolve operation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var depthResolveFilter: MTLMultisampleDepthResolveFilter { get set }
```

#### Discussion

The default value is [`MTLMultisampleDepthResolveFilter.sample0`](mtlmultisampledepthresolvefilter/sample0.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor/depthresolvefilter)*