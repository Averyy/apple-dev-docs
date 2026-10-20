# requestedScopes

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The contact information to be requested from the user during authentication.

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
var requestedScopes: [ASAuthorization.Scope]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<NSString *> * requestedScopes;
```

## See Also

### Setting the Scope
- [ASAuthorization.Scope](../asauthorization/scope.md)
  The kinds of contact information that can be requested from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationopenidrequest/requestedscopes)*