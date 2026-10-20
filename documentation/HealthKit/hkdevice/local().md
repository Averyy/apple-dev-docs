# local()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

returns a device object that represents the current device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func local() -> HKDevice
```

```objc
+ (HKDevice *) localDevice;
```

#### Return Value

A device object representing the hardware (iPhone, iPod Touch, or Apple Watch) that is running the app.

## See Also

### Creating Device Objects
- [init(name: String?, manufacturer: String?, model: String?, hardwareVersion: String?, firmwareVersion: String?, softwareVersion: String?, localIdentifier: String?, udiDeviceIdentifier: String?)](./init%28name,manufacturer,model,hardwareversion,firmwareversion,softwareversion,localidentifier,udideviceidentifier%29-3663q.md)
  Initializes a new device object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdevice/local())*