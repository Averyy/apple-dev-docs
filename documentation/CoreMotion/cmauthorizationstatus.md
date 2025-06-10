# CMAuthorizationStatus

**Framework**: Core Motion  
**Kind**: enum

The authorization status for motion-related features.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum CMAuthorizationStatus
```

## Topics

### Enumeration Cases
- [CMAuthorizationStatus.notDetermined](cmauthorizationstatus/notdetermined.md)
  The status has not yet been determined.
- [CMAuthorizationStatus.restricted](cmauthorizationstatus/restricted.md)
  Access is denied due to system-wide restrictions.
- [CMAuthorizationStatus.denied](cmauthorizationstatus/denied.md)
  Access was denied by the user.
- [CMAuthorizationStatus.authorized](cmauthorizationstatus/authorized.md)
  Access was granted by the user.
### Initializers
- [init?(rawValue: Int)](cmauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func isAbsoluteAltitudeAvailable() -> Bool](cmaltimeter/isabsolutealtitudeavailable.md)
  Returns a Boolean value indicating whether the current device reports changes in the absolute altitude.
- [class func isRelativeAltitudeAvailable() -> Bool](cmaltimeter/isrelativealtitudeavailable.md)
  Returns a Boolean value indicating whether the current device supports generating data for relative altitude changes.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmaltimeter/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to retrieve altimeter data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)*