# MTLGPUFamily

**Framework**: Metal  
**Kind**: enum

Represents the functionality for families of GPUs.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLGPUFamily
```

## Mentions

- [Detecting GPU features and Metal software versions](detecting-gpu-features-and-metal-software-versions.md)
- [Improving your game’s graphics performance and settings](improving-your-games-graphics-performance-and-settings.md)

#### Overview

Check whether a GPU supports the features of a specific family by calling the [`supportsFamily(_:)`](mtldevice/supportsfamily(_:).md) method of a GPU’s [`MTLDevice`](mtldevice.md) instance.

## Topics

### Checking for Metal family GPU support
- [MTLGPUFamily.metal4](mtlgpufamily/metal4.md)
- [MTLGPUFamily.metal3](mtlgpufamily/metal3.md)
  Represents the Metal 3 features.
### Checking for Apple family GPU support
- [MTLGPUFamily.apple9](mtlgpufamily/apple9.md)
  Represents the Apple family 9 GPU features that correspond to the Apple A17, M3, and M4 GPUs.
- [MTLGPUFamily.apple8](mtlgpufamily/apple8.md)
  Represents the Apple family 8 GPU features that correspond to the Apple A15, A16, and M2 GPUs.
- [MTLGPUFamily.apple7](mtlgpufamily/apple7.md)
  Represents the Apple family 7 GPU features that correspond to the Apple A14 and M1 GPUs.
- [MTLGPUFamily.apple6](mtlgpufamily/apple6.md)
  Represents the Apple family 6 GPU features that correspond to the Apple A13 GPUs.
- [MTLGPUFamily.apple5](mtlgpufamily/apple5.md)
  Represents the Apple family 5 GPU features that correspond to the Apple A12 GPUs.
- [MTLGPUFamily.apple4](mtlgpufamily/apple4.md)
  Represents the Apple family 4 GPU features that correspond to the Apple A11 GPUs.
- [MTLGPUFamily.apple3](mtlgpufamily/apple3.md)
  Represents the Apple family 3 GPU features that correspond to the Apple A9 and A10 GPUs.
- [MTLGPUFamily.apple2](mtlgpufamily/apple2.md)
  Represents the Apple family 2 GPU features that correspond to the Apple A8 GPUs.
- [MTLGPUFamily.apple1](mtlgpufamily/apple1.md)
  Represents the Apple family 1 GPU features that correspond to the Apple A7 GPUs.
### Checking for common GPU support
- [MTLGPUFamily.common3](mtlgpufamily/common3.md)
  Represents the Common family 3 GPU features.
- [MTLGPUFamily.common2](mtlgpufamily/common2.md)
  Represents the Common family 2 GPU features.
- [MTLGPUFamily.common1](mtlgpufamily/common1.md)
  Represents the Common family 1 GPU features.
### Checking for macOS family GPU support
- [MTLGPUFamily.mac2](mtlgpufamily/mac2.md)
  Represents the Mac family 2 GPU features.
- [MTLGPUFamily.mac1](mtlgpufamily/mac1.md)
  Represents the Mac family 1 GPU features.
### Checking for Mac Catalyst family GPU support
- [MTLGPUFamily.macCatalyst2](mtlgpufamily/maccatalyst2.md)
  Represents a family 2 Mac GPU when running an app you built with Mac Catalyst.
- [MTLGPUFamily.macCatalyst1](mtlgpufamily/maccatalyst1.md)
  Represents a family 1 Mac GPU when running an app you built with Mac Catalyst.
### Swift support
- [init?(rawValue: Int)](mtlgpufamily/init(rawvalue:).md)
  Creates a GPU family instance from a raw value.
### Enumeration Cases
- [MTLGPUFamily.apple10](mtlgpufamily/apple10.md)

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
- [func supportsFeatureSet(MTLFeatureSet) -> Bool](mtldevice/supportsfeatureset(_:).md)
  Returns a Boolean value that indicates whether the GPU device supports a specific feature set.
- [enum MTLFeatureSet](mtlfeatureset.md)
  The device feature sets that define specific platform, hardware, and software configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlgpufamily)*