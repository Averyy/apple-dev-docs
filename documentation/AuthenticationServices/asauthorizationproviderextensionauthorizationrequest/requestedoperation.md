# requestedOperation

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The operation for the extension to execute.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var requestedOperation: ASAuthorizationProviderAuthorizationOperation { get }
```

```objc
@property (nonatomic, readonly) ASAuthorizationProviderAuthorizationOperation requestedOperation;
```

## See Also

### Parsing the Request
- [var url: URL](./url.md)
  The complete URL of the request, including all components.
- [var httpHeaders: [String : String]](./httpheaders.md)
  The HTTP headers of the request.
- [var httpBody: Data](./httpbody.md)
  The HTTP body of the request.
- [var realm: String](./realm.md)
  The realm to which the request applies.
- [struct ASAuthorizationProviderAuthorizationOperation](../asauthorizationproviderauthorizationoperation.md)
  A type that represents an authorization operation.
- [var authorizationOptions: [AnyHashable : Any]](./authorizationoptions.md)
  A collection of options associated with the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/requestedoperation)*