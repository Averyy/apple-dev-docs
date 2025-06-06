# device

**Framework**: Core Animation  
**Kind**: property

The Metal device responsible for the layer’s drawable resources.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var device: (any MTLDevice)? { get set }
```

#### Discussion

This property determines which device object Metal uses to create its [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) objects. When you retrieve a drawable object and its associated texture, you must render to the texture using the same device object.

The default value is `nil`—you must set the device for a layer before rendering.

## See Also

- [Core Animation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [var preferredDevice: (any MTLDevice)?](cametallayer/preferreddevice.md)
  The device object that the system recommends using for this layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/device)*