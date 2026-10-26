# cpuCacheModeWriteCombined

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

A write-combined CPU cache mode that is optimized for resources that the CPU writes into, but never reads.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var cpuCacheModeWriteCombined: MTLResourceOptions { get }
```

```c
MTLResourceCPUCacheModeWriteCombined
```

## See Also

### Specifying CPU cache modes
- [MTLResourceCPUCacheModeDefaultCache](./mtlresourcecpucachemodedefaultcache.md)
  The default CPU cache mode for the resource, which guarantees that read and write operations are executed in the expected order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceoptions/cpucachemodewritecombined)*