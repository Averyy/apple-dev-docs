# supportsFeatureSet(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the GPU device supports a specific feature set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func supportsFeatureSet(_ featureSet: MTLFeatureSet) -> Bool
```

## Parameters

- `featureSet`: A   instance.

## See Also

- [Detecting GPU Features and Metal Software Versions](detecting-gpu-features-and-metal-software-versions.md)
  Use the device object’s properties to determine how you perform tasks in Metal.
- [func supportsFamily(MTLGPUFamily) -> Bool](mtldevice/supportsfamily(_:).md)
  Returns a Boolean value that indicates whether the GPU device supports the feature set of a specific GPU family.
- [enum MTLGPUFamily](mtlgpufamily.md)
  Represents the functionality for families of GPUs.
- [enum MTLFeatureSet](mtlfeatureset.md)
  The device feature sets that define specific platform, hardware, and software configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportsfeatureset(_:))*