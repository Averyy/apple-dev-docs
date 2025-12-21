# MTLFeatureSet

**Framework**: Metal  
**Kind**: enum

The device feature sets that define specific platform, hardware, and software configurations.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLFeatureSet
```

#### Overview

If your app is running on an operating system that supports the [`supportsFamily(_:)`](mtldevice/supportsfamily(_:).md) method, use that method instead. See [`Detecting GPU features and Metal software versions`](detecting-gpu-features-and-metal-software-versions.md) for more information about [`MTLGPUFamily`](mtlgpufamily.md) — the replacement for this enumeration —  and the feature set tables. This type doesn’t define constants for GPU families introduced after iOS GPU family 5.

Metal feature sets define the feature availability, implementation limits, and pixel format capabilities for each device. The table shows the GPU families and their corresponding GPU hardware.

| GPU family | GPU hardware |
| --- | --- |
| iOS GPU family 1 | Apple A7 devices |
| iOS GPU family 2 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) tvOS GPU family 1 | Apple A8 devices |
| iOS GPU family 3 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) tvOS GPU family 2 | Apple A9 devices ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Apple A10 devices |
| iOS GPU family 4 | Apple A11 devices |
| iOS GPU family 5 | Apple A12 devices |
| macOS GPU family 1 | iMac Pro models ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) iMac models from 2012 or later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) MacBook models from 2015 or later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) MacBook Pro models from 2012 or later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) MacBook Air models from 2012 or later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Mac mini models from 2012 or later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Mac Pro models from late 2013 |
| macOS GPU family 2 | iMac models from 2015 or later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) MacBook Pro models from 2016 or later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) MacBook models from 2016 or later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) iMac Pro models from 2017 or later |

For more information on Mac support for Metal, see [`Mac computers that support Metal`](https://developer.apple.comhttps://support.apple.com/en-us/HT205073).

## Topics

### iOS GPU family 5
- [MTLFeatureSet.iOS_GPUFamily5_v1](mtlfeatureset/ios_gpufamily5_v1.md)
  The GPU family 5, version 1 feature set for iOS.
### iOS GPU family 4
- [MTLFeatureSet.iOS_GPUFamily4_v2](mtlfeatureset/ios_gpufamily4_v2.md)
  The GPU family 4, version 2 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily4_v1](mtlfeatureset/ios_gpufamily4_v1.md)
  The GPU family 4, version 1 feature set for iOS.
### iOS GPU family 3
- [MTLFeatureSet.iOS_GPUFamily3_v4](mtlfeatureset/ios_gpufamily3_v4.md)
  The GPU family 3, version 4 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily3_v3](mtlfeatureset/ios_gpufamily3_v3.md)
  The GPU family 3, version 3 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily3_v2](mtlfeatureset/ios_gpufamily3_v2.md)
  The GPU family 3, version 2 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily3_v1](mtlfeatureset/ios_gpufamily3_v1.md)
  The GPU family 3, version 1 feature set for iOS.
### iOS GPU family 2
- [MTLFeatureSet.iOS_GPUFamily2_v5](mtlfeatureset/ios_gpufamily2_v5.md)
  The GPU family 2, version 5 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily2_v4](mtlfeatureset/ios_gpufamily2_v4.md)
  The GPU family 2, version 4 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily2_v3](mtlfeatureset/ios_gpufamily2_v3.md)
  The GPU family 2, version 3 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily2_v2](mtlfeatureset/ios_gpufamily2_v2.md)
  The GPU family 2, version 2 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily2_v1](mtlfeatureset/ios_gpufamily2_v1.md)
  The GPU family 2, version 1 feature set for iOS.
### iOS GPU family 1
- [MTLFeatureSet.iOS_GPUFamily1_v5](mtlfeatureset/ios_gpufamily1_v5.md)
  The GPU family 1, version 5 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily1_v4](mtlfeatureset/ios_gpufamily1_v4.md)
  The GPU family 1, version 4 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily1_v3](mtlfeatureset/ios_gpufamily1_v3.md)
  The GPU family 1, version 3 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily1_v2](mtlfeatureset/ios_gpufamily1_v2.md)
  The GPU family 1, version 2 feature set for iOS.
- [MTLFeatureSet.iOS_GPUFamily1_v1](mtlfeatureset/ios_gpufamily1_v1.md)
  The GPU family 1, version 1 feature set for iOS.
### tvOS GPU family 2
- [MTLFeatureSet.tvOS_GPUFamily2_v2](mtlfeatureset/tvos_gpufamily2_v2.md)
  The GPU family 2, version 2 feature set for tvOS.
- [MTLFeatureSet.tvOS_GPUFamily2_v1](mtlfeatureset/tvos_gpufamily2_v1.md)
  The GPU family 2, version 1 feature set for tvOS.
### tvOS GPU family 1
- [MTLFeatureSet.tvOS_GPUFamily1_v4](mtlfeatureset/tvos_gpufamily1_v4.md)
  The GPU family 1, version 4 feature set for tvOS.
- [MTLFeatureSet.tvOS_GPUFamily1_v3](mtlfeatureset/tvos_gpufamily1_v3.md)
  The GPU family 1, version 3 feature set for tvOS.
- [MTLFeatureSet.tvOS_GPUFamily1_v2](mtlfeatureset/tvos_gpufamily1_v2.md)
  The GPU family 1, version 2 feature set for tvOS.
- [MTLFeatureSet.tvOS_GPUFamily1_v1](mtlfeatureset/tvos_gpufamily1_v1-swift.enum.case.md)
  The GPU family 1, version 1 feature set for tvOS.
### macOS GPU family 2
- [MTLFeatureSet.macOS_GPUFamily2_v1](mtlfeatureset/macos_gpufamily2_v1.md)
  The GPU family 2, version 1 feature set for macOS.
### macOS GPU family 1
- [MTLFeatureSet.macOS_GPUFamily1_v4](mtlfeatureset/macos_gpufamily1_v4.md)
  The GPU family 1, version 4 feature set for macOS.
- [MTLFeatureSet.macOS_GPUFamily1_v3](mtlfeatureset/macos_gpufamily1_v3.md)
  The GPU family 1, version 3 feature set for macOS.
- [MTLFeatureSet.macOS_GPUFamily1_v2](mtlfeatureset/macos_gpufamily1_v2.md)
  The GPU family 1, version 2 feature set for macOS.
- [MTLFeatureSet.macOS_GPUFamily1_v1](mtlfeatureset/macos_gpufamily1_v1.md)
  The GPU family 1, version 1 feature set for macOS.
### macOS tier 2
- [MTLFeatureSet.macOS_ReadWriteTextureTier2](mtlfeatureset/macos_readwritetexturetier2.md)
  The read-write texture, tier 2 feature set for macOS.
### Initializers
- [init?(rawValue: UInt)](mtlfeatureset/init(rawvalue:).md)
### Type Properties
- [static var osx_GPUFamily1_v1: MTLFeatureSet](mtlfeatureset/osx_gpufamily1_v1.md)
- [static var osx_GPUFamily1_v2: MTLFeatureSet](mtlfeatureset/osx_gpufamily1_v2.md)
- [static var osx_ReadWriteTextureTier2: MTLFeatureSet](mtlfeatureset/osx_readwritetexturetier2.md)
- [static var tvos_GPUFamily1_v1: MTLFeatureSet](mtlfeatureset/tvos_gpufamily1_v1-swift.type.property.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func supportsFamily(MTLGPUFamily) -> Bool](mtldevice/supportsfamily(_:).md)
  Returns a Boolean value that indicates whether the GPU device supports the feature set of a specific GPU family.
- [enum MTLGPUFamily](mtlgpufamily.md)
  Represents the functionality for families of GPUs.
- [func supportsFeatureSet(MTLFeatureSet) -> Bool](mtldevice/supportsfeatureset(_:).md)
  Returns a Boolean value that indicates whether the GPU device supports a specific feature set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfeatureset)*