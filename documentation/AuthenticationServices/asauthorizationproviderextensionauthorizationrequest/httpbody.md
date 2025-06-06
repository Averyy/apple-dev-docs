# httpBody

**Framework**: Authentication Services  
**Kind**: property

The HTTP body of the request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var httpBody: Data { get }
```

## See Also

- [var url: URL](asauthorizationproviderextensionauthorizationrequest/url.md)
  The complete URL of the request, including all components.
- [var httpHeaders: [String : String]](asauthorizationproviderextensionauthorizationrequest/httpheaders.md)
  The HTTP headers of the request.
- [var realm: String](asauthorizationproviderextensionauthorizationrequest/realm.md)
  The realm to which the request applies.
- [var requestedOperation: ASAuthorizationProviderAuthorizationOperation](asauthorizationproviderextensionauthorizationrequest/requestedoperation.md)
  The operation for the extension to execute.
- [struct ASAuthorizationProviderAuthorizationOperation](asauthorizationproviderauthorizationoperation.md)
  A type that represents an authorization operation.
- [var authorizationOptions: [AnyHashable : Any]](asauthorizationproviderextensionauthorizationrequest/authorizationoptions.md)
  A collection of options associated with the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/httpbody)*