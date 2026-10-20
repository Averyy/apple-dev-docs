# authorizationStatus

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The authorization status for receiving fall detection event notifications.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
var authorizationStatus: CMAuthorizationStatus { get }
```

```objc
@property (nonatomic, readonly) CMAuthorizationStatus authorizationStatus;
```

## See Also

### Requesting Authorization
- [func requestAuthorization(handler: (CMAuthorizationStatus) -> Void)](./requestauthorization%28handler%29.md)
  Requests authorization to receive notifications about fall detection events.
- [enum CMAuthorizationStatus](../cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/authorizationstatus)*