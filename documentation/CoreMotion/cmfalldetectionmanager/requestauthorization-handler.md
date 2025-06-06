# requestAuthorization(handler:)

**Framework**: Core Motion  
**Kind**: method

Requests authorization to receive notifications about fall detection events.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
func requestAuthorization(handler: @escaping (CMAuthorizationStatus) -> Void)
```

#### Discussion

As soon as the user authorizes fall detection, the system calls the delegate’s [`fallDetectionManager(_:didDetect:completionHandler:)`](cmfalldetectiondelegate/falldetectionmanager(_:diddetect:completionhandler:).md) method and passes the latest fall detection event.

## Parameters

- `handler`: The system passes the following parameter:

## See Also

- [var authorizationStatus: CMAuthorizationStatus](cmfalldetectionmanager/authorizationstatus.md)
  The authorization status for receiving fall detection event notifications.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:))*