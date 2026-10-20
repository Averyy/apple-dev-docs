# storageBehaviorConfiguration

**Framework**: Matter  
**Kind**: property  
**Role**: Instance Property

Sets the storage behavior configuration - see MTRDeviceStorageBehaviorConfiguration.h for details

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
@NSCopying
var storageBehaviorConfiguration: MTRDeviceStorageBehaviorConfiguration? { get set }
```

```objc
@property (nonatomic, copy, nullable) MTRDeviceStorageBehaviorConfiguration * storageBehaviorConfiguration;
```

#### Discussion

If this value is nil, a default storage behavior configuration will be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerparameters/storagebehaviorconfiguration)*