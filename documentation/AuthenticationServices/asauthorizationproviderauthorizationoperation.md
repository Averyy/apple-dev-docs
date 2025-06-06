# ASAuthorizationProviderAuthorizationOperation

**Framework**: Authentication Services  
**Kind**: struct

A type that represents an authorization operation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct ASAuthorizationProviderAuthorizationOperation
```

## Topics

### Handling Configuration Removal
- [static let configurationRemoved: ASAuthorizationProviderAuthorizationOperation](asauthorizationproviderauthorizationoperation/configurationremoved.md)
  An operation the system invokes when the extension configuration is removed from the system.
### Creating Operations
- [init(String)](asauthorizationproviderauthorizationoperation/init(_:).md)
  Creates an authorization operation using the specified string value.
- [init(rawValue: String)](asauthorizationproviderauthorizationoperation/init(rawvalue:).md)
  Creates an authorization operation using the specified raw string value.
### Type Properties
- [static let directRequest: ASAuthorizationProviderAuthorizationOperation](asauthorizationproviderauthorizationoperation/directrequest.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var url: URL](asauthorizationproviderextensionauthorizationrequest/url.md)
  The complete URL of the request, including all components.
- [var httpHeaders: [String : String]](asauthorizationproviderextensionauthorizationrequest/httpheaders.md)
  The HTTP headers of the request.
- [var httpBody: Data](asauthorizationproviderextensionauthorizationrequest/httpbody.md)
  The HTTP body of the request.
- [var realm: String](asauthorizationproviderextensionauthorizationrequest/realm.md)
  The realm to which the request applies.
- [var requestedOperation: ASAuthorizationProviderAuthorizationOperation](asauthorizationproviderextensionauthorizationrequest/requestedoperation.md)
  The operation for the extension to execute.
- [var authorizationOptions: [AnyHashable : Any]](asauthorizationproviderextensionauthorizationrequest/authorizationoptions.md)
  A collection of options associated with the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderauthorizationoperation)*