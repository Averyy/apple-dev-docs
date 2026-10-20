# authorizationStatus

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Your app’s authorization status for the external storage device.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class var authorizationStatus: AVAuthorizationStatus { get }
```

```objc
@property (class, readonly) AVAuthorizationStatus authorizationStatus;
```

#### Discussion

If the value is [`AVAuthorizationStatus.notDetermined`](../avauthorizationstatus/notdetermined.md), you can request access by calling the [`requestAccess(completionHandler:)`](./requestaccess%28completionhandler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/authorizationstatus)*