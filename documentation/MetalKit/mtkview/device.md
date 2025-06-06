# device

**Framework**: MetalKit  
**Kind**: property

The device object the view uses to create its Metal objects.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var device: (any MTLDevice)? { get set }
```

#### Discussion

The default value is `nil`. You must explicitly set the device object.

## See Also

- [var preferredDevice: (any MTLDevice)?](mtkview/preferreddevice.md)
  The device object that the system recommends using for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/device)*