# requestAuthorization(handler:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Requests authorization to receive notifications about fall detection events.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
func requestAuthorization(handler: @escaping (CMAuthorizationStatus) -> Void)
```

```objc
- (void) requestAuthorizationWithHandler:(void (^)(CMAuthorizationStatus status)) handler;
```

#### Discussion

As soon as the user authorizes fall detection, the system calls the delegate’s [`fallDetectionManager(_:didDetect:completionHandler:)`](../cmfalldetectiondelegate/falldetectionmanager%28_,diddetect,completionhandler%29.md) method and passes the latest fall detection event.

## Parameters

- `handler`: A block that is called by the system after the user accepts or declines the authorization request.

  The system passes the following parameter:

  - **`status`**: The authorization status chosen by the user.

## See Also

### Requesting Authorization
- [var authorizationStatus: CMAuthorizationStatus](./authorizationstatus.md)
  The authorization status for receiving fall detection event notifications.
- [enum CMAuthorizationStatus](../cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:))*