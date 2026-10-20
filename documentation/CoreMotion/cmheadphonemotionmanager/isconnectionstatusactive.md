# isConnectionStatusActive

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- watchOS 7.0+

## Declaration

```swift
var isConnectionStatusActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isConnectionStatusActive) BOOL connectionStatusActive;
```

## See Also

### Checking Availability
- [var isDeviceMotionAvailable: Bool](./isdevicemotionavailable.md)
  A Boolean value that indicates whether the current device supports the headphone motion manager.
- [var isDeviceMotionActive: Bool](./isdevicemotionactive.md)
  A Boolean value that indicates whether the headphone motion manager is active.
- [class func authorizationStatus() -> CMAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns the authorization status for monitoring headphone motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/isconnectionstatusactive)*