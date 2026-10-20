# requestedOperation

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The OpenID authentication operation you want this request to perform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var requestedOperation: ASAuthorization.OpenIDOperation { get set }
```

```objc
@property (nonatomic, copy) ASAuthorizationOpenIDOperation requestedOperation;
```

## See Also

### Setting the Operation
- [ASAuthorization.OpenIDOperation](../asauthorization/openidoperation.md)
  The kinds of operations that you can perform with OpenID authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationopenidrequest/requestedoperation)*