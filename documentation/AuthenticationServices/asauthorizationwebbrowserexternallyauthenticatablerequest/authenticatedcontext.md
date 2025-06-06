# authenticatedContext

**Framework**: Authentication Services  
**Kind**: property  
**Required**: Yes

The local authentication context for the authorization.

**Availability**:
- macOS 13.3+

## Declaration

```swift
var authenticatedContext: LAContext? { get set }
```

#### Discussion

Ensure the person authenticates, for example using FaceID, before accessing their credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserexternallyauthenticatablerequest/authenticatedcontext)*