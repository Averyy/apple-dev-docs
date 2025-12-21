# cpuCacheMode

**Framework**: Metal  
**Kind**: property

A value that configures the cache mode of CPU mapping of tensors you create with this descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var cpuCacheMode: MTLCPUCacheMode { get set }
```

#### Discussion

The default value of this property is [`MTLCPUCacheMode.defaultCache`](mtlcpucachemode/defaultcache.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/cpucachemode)*