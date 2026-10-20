# capabilities

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The capabilities of the device as reported by the device module.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var capabilities: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * capabilities;
```

## See Also

### Inspecting a Device’s Capabilities
- [struct ICDeviceCapability](../icdevicecapability.md)
  Constants that describe the capabilities of a camera.
- [struct ICSessionOptions](../icsessionoptions.md)
  Session options for altering the delivery of the device contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/capabilities)*