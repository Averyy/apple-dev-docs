# ICSessionOptions

**Framework**: ImageCaptureCore  
**Kind**: struct  
**Role**: Structure

Session options for altering the delivery of the device contents.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct ICSessionOptions
```

```c
typedef NSString * ICSessionOptions;
```

## Topics

### Initializers
- [init(rawValue: String)](./icsessionoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting a Device’s Capabilities
- [var capabilities: [String]](./icdevice/capabilities.md)
  The capabilities of the device as reported by the device module.
- [struct ICDeviceCapability](./icdevicecapability.md)
  Constants that describe the capabilities of a camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icsessionoptions)*