# device

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The device object that created the sampler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

#### Discussion

A sampler is always associated with the [`MTLDevice`](mtldevice.md) that created it and can be used only with that device.

## See Also

- [var label: String?](mtlsamplerstate/label.md)
  A string that identifies the sampler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerstate/device)*