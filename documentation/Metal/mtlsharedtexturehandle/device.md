# device

**Framework**: Metal  
**Kind**: property

The device object that created the texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

#### Discussion

A texture is always associated with the [`MTLDevice`](mtldevice.md) that created it and can be used only with that device.

## See Also

- [var label: String?](mtlsharedtexturehandle/label.md)
  A string that identifies the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedtexturehandle/device)*