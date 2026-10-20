# isPrimaryConstituentDeviceSwitchingBehaviorLockedWithDeviceSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Whether locking to a particular primary constituent device is supported.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var isPrimaryConstituentDeviceSwitchingBehaviorLockedWithDeviceSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPrimaryConstituentDeviceSwitchingBehaviorLockedWithDeviceSupported) BOOL primaryConstituentDeviceSwitchingBehaviorLockedWithDeviceSupported;
```

#### Discussion

This property returns `true` if [`setPrimaryConstituentDeviceSwitchingBehaviorLockedWith(_:)`](./setprimaryconstituentdeviceswitchingbehaviorlockedwith%28_%29.md) is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isprimaryconstituentdeviceswitchingbehaviorlockedwithdevicesupported)*