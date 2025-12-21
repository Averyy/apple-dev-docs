# isActivityAvailable()

**Framework**: Core Motion  
**Kind**: method

Returns a Boolean indicating whether motion data is available on the current device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
class func isActivityAvailable() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if motion data is available or [`false`](https://developer.apple.com/documentation/Swift/false) if it is not.

#### Discussion

Motion data is not available on all iOS devices. Use this method to determine if support is available on the current device.

## See Also

- [class func authorizationStatus() -> CMAuthorizationStatus](cmmotionactivitymanager/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to retrieve stored motion data.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/isactivityavailable())*