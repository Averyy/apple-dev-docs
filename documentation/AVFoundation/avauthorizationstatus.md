# AVAuthorizationStatus

**Framework**: AVFoundation  
**Kind**: enum

Constants that indicate the status of an app’s authorization to capture media.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.14+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum AVAuthorizationStatus
```

#### Overview

Call [`authorizationStatus(for:)`](avcapturedevice/authorizationstatus(for:).md) to determine the app’s current permission to capture media.

## Topics

### Status Values
- [AVAuthorizationStatus.notDetermined](avauthorizationstatus/notdetermined.md)
  A status that indicates the user hasn’t yet granted or denied authorization.
- [AVAuthorizationStatus.restricted](avauthorizationstatus/restricted.md)
  A status that indicates the app isn’t permitted to use media capture devices.
- [AVAuthorizationStatus.denied](avauthorizationstatus/denied.md)
  A status that indicates the user has explicitly denied an app permission to capture media.
- [AVAuthorizationStatus.authorized](avauthorizationstatus/authorized.md)
  A status that indicates the user has explicitly granted an app permission to capture media.
### Initializers
- [init?(rawValue: Int)](avauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func requestAccess(for: AVMediaType, completionHandler: (Bool) -> Void)](avcapturedevice/requestaccess(for:completionhandler:).md)
  Requests the user’s permission to allow the app to capture media of a particular type.
- [class func authorizationStatus(for: AVMediaType) -> AVAuthorizationStatus](avcapturedevice/authorizationstatus(for:).md)
  Returns an authorization status that indicates whether the user grants the app permission to capture media of a particular type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus)*