# supportsFeatureSet(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether the GPU device supports a specific feature set.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`supportsFamily(_:)`](./supportsfamily%28_%29.md) method instead if your app is running on an OS that supports that method.

## Declaration

```swift
func supportsFeatureSet(_ featureSet: MTLFeatureSet) -> Bool
```

```objc
- (BOOL) supportsFeatureSet:(MTLFeatureSet) featureSet;
```

## Parameters

- `featureSet`: An [`MTLFeatureSet`](../mtlfeatureset.md) instance.

## See Also

### Related Documentation
- [Detecting GPU features and Metal software versions](../detecting-gpu-features-and-metal-software-versions.md)
  Use the device object’s properties to determine how you perform tasks in Metal.
### Checking a GPU device’s feature support
- [func supportsFamily(MTLGPUFamily) -> Bool](./supportsfamily%28_%29.md)
  Returns a Boolean value that indicates whether the GPU device supports the feature set of a specific GPU family.
- [enum MTLGPUFamily](../mtlgpufamily.md)
  Represents the functionality for families of GPUs.
- [enum MTLFeatureSet](../mtlfeatureset.md)
  The device feature sets that define specific platform, hardware, and software configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportsfeatureset(_:))*