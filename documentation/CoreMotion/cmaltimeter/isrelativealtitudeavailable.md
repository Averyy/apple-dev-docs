# isRelativeAltitudeAvailable()

**Framework**: Core Motion  
**Kind**: method

Returns a Boolean value indicating whether the current device supports generating data for relative altitude changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
class func isRelativeAltitudeAvailable() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the device supports relative altitude changes or [`false`](https://developer.apple.com/documentation/swift/false) if it does not.

#### Discussion

Use this method to determine if altitude updates are available before calling the [`startRelativeAltitudeUpdates(to:withHandler:)`](cmaltimeter/startrelativealtitudeupdates(to:withhandler:).md) method.

## See Also

- [class func isAbsoluteAltitudeAvailable() -> Bool](cmaltimeter/isabsolutealtitudeavailable.md)
  Returns a Boolean value indicating whether the current device reports changes in the absolute altitude.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmaltimeter/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to retrieve altimeter data.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable())*