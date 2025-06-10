# isAbsoluteAltitudeAvailable()

**Framework**: Core Motion  
**Kind**: method

Returns a Boolean value indicating whether the current device reports changes in the absolute altitude.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- watchOS 8.0+

## Declaration

```swift
class func isAbsoluteAltitudeAvailable() -> Bool
```

#### Discussion

Use this method to determine if altitude updates are available before calling the [`startAbsoluteAltitudeUpdates(to:withHandler:)`](cmaltimeter/startabsolutealtitudeupdates(to:withhandler:).md) method.

> **Note**:  Absolute altitude is only available on iPhone 12 and later and Apple Watch 6 or SE and later.

## See Also

- [class func isRelativeAltitudeAvailable() -> Bool](cmaltimeter/isrelativealtitudeavailable.md)
  Returns a Boolean value indicating whether the current device supports generating data for relative altitude changes.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmaltimeter/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to retrieve altimeter data.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltimeter/isabsolutealtitudeavailable())*