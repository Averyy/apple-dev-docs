# device

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) id<MTLDevice> device;
```

#### Discussion

A texture is always associated with the [`MTLDevice`](../mtldevice.md) that created it and can be used only with that device.

## See Also

### Identifying the shared texture handle
- [var label: String?](./label.md)
  A string that identifies the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedtexturehandle/device)*