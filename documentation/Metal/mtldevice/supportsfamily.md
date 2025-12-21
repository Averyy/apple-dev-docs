# supportsFamily(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the GPU device supports the feature set of a specific GPU family.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func supportsFamily(_ gpuFamily: MTLGPUFamily) -> Bool
```

## Mentions

- [Improving your game’s graphics performance and settings](improving-your-games-graphics-performance-and-settings.md)
- [Choosing a resource storage mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
- [Setting resource storage modes](setting-resource-storage-modes.md)

## Parameters

- `gpuFamily`: An   instance.

## See Also

- [enum MTLGPUFamily](mtlgpufamily.md)
  Represents the functionality for families of GPUs.
- [func supportsFeatureSet(MTLFeatureSet) -> Bool](mtldevice/supportsfeatureset(_:).md)
  Returns a Boolean value that indicates whether the GPU device supports a specific feature set.
- [enum MTLFeatureSet](mtlfeatureset.md)
  The device feature sets that define specific platform, hardware, and software configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportsfamily(_:))*