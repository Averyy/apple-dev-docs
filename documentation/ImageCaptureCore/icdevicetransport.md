# ICDeviceTransport

**Framework**: ImageCaptureCore  
**Kind**: struct  
**Role**: Structure

The hardware connection types a device can use.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
struct ICDeviceTransport
```

```c
typedef NSString * ICDeviceTransport;
```

## Topics

### Initializers
- [init(rawValue: String)](./icdevicetransport/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting a Device’s Transport Type
- [var transportType: String?](./icdevice/transporttype.md)
  The hardware connection type the device is using.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicetransport)*