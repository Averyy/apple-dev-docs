# deviceMotion

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The latest device-motion data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- watchOS 7.0+

## Declaration

```swift
var deviceMotion: CMDeviceMotion? { get }
```

```objc
@property (readonly, nullable) CMDeviceMotion * deviceMotion;
```

#### Discussion

This property is `nil` when there is no device-motion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotion)*