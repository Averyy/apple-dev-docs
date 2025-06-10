# cpuCacheMode

**Framework**: Metal  
**Kind**: property

A value that configures the cache mode of CPU mapping of tensors you create with this descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var cpuCacheMode: MTLCPUCacheMode { get set }
```

#### Discussion

The default value of this property is [`MTLCPUCacheMode.defaultCache`](mtlcpucachemode/defaultcache.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/cpucachemode)*