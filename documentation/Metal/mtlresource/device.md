# device

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The device object that created the resource.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

```objc
@property (readonly) id<MTLDevice> device;
```

#### Discussion

A resource can only be used with the [`MTLDevice`](../mtldevice.md) that created it.

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
### Identifying the resource
- [var label: String?](./label.md)
  A string that identifies the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/device)*