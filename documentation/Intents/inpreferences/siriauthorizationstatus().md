# siriAuthorizationStatus()

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Returns the current authorization status of your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func siriAuthorizationStatus() -> INSiriAuthorizationStatus
```

```objc
+ (INSiriAuthorizationStatus) siriAuthorizationStatus;
```

## Return Value

The authorization status of your app.

## Discussion

Use this method to determine if your app is authorized to interact with Siri. The user can disable Siri behaviors for specific apps or for all apps. The user can change the authorization for apps in the Siri section of the system settings.

## See Also

### Managing the App’s Authorization
- [class func requestSiriAuthorization((INSiriAuthorizationStatus) -> Void)](./requestsiriauthorization%28_%29.md)
  Requests authorization to use Siri services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpreferences/siriauthorizationstatus())*