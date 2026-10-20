# currentVerticalTilt

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

Characteristic corresponding to the camera’s current vertical tilt setting.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var currentVerticalTilt: HMCharacteristic? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) HMCharacteristic * currentVerticalTilt;
```

## See Also

### Controlling camera characteristics
- [var currentHorizontalTilt: HMCharacteristic?](./currenthorizontaltilt.md)
  Characteristic corresponding to the camera’s current horizontal tilt setting.
- [var targetHorizontalTilt: HMCharacteristic?](./targethorizontaltilt.md)
  Characteristic corresponding to adjusting the camera’s horizontal tilt setting.
- [var targetVerticalTilt: HMCharacteristic?](./targetverticaltilt.md)
  Characteristic corresponding to adjusting the camera’s vertical tilt setting.
- [var opticalZoom: HMCharacteristic?](./opticalzoom.md)
  Characteristic corresponding to the camera’s optical zoom setting.
- [var digitalZoom: HMCharacteristic?](./digitalzoom.md)
  Characteristic corresponding to the camera’s digital zoom setting.
- [var imageMirroring: HMCharacteristic?](./imagemirroring.md)
  Characteristic corresponding to the camera’s image mirroring setting.
- [var imageRotation: HMCharacteristic?](./imagerotation.md)
  Characteristic corresponding to the camera’s image rotation setting.
- [var nightVision: HMCharacteristic?](./nightvision.md)
  Characteristic corresponding to the camera’s night vision setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol/currentverticaltilt)*