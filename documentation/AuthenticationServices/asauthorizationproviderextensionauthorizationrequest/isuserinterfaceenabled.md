# isUserInterfaceEnabled

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

Determines if user interface is available for the current request.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- visionOS 1.0+

## Declaration

```swift
var isUserInterfaceEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isUserInterfaceEnabled) BOOL userInterfaceEnabled;
```

## Discussion

If this value is `false`, then calls to [`presentAuthorizationViewController(completion:)`](./presentauthorizationviewcontroller%28completion%29.md) fail and the system cancels the request.

## See Also

### Interacting with the User
- [func presentAuthorizationViewController(completion: (Bool, (any Error)?) -> Void)](./presentauthorizationviewcontroller%28completion%29.md)
  Asks the authorization service to show the extension’s view controller to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/isuserinterfaceenabled)*