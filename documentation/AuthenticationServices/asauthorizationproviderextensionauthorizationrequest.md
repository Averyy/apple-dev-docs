# ASAuthorizationProviderExtensionAuthorizationRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

An authorization request that your provider extension handles.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationProviderExtensionAuthorizationRequest
```

```objc
@interface ASAuthorizationProviderExtensionAuthorizationRequest : NSObject
```

## Topics

### Parsing the Request
- [var url: URL](./asauthorizationproviderextensionauthorizationrequest/url.md)
  The complete URL of the request, including all components.
- [var httpHeaders: [String : String]](./asauthorizationproviderextensionauthorizationrequest/httpheaders.md)
  The HTTP headers of the request.
- [var httpBody: Data](./asauthorizationproviderextensionauthorizationrequest/httpbody.md)
  The HTTP body of the request.
- [var realm: String](./asauthorizationproviderextensionauthorizationrequest/realm.md)
  The realm to which the request applies.
- [var requestedOperation: ASAuthorizationProviderAuthorizationOperation](./asauthorizationproviderextensionauthorizationrequest/requestedoperation.md)
  The operation for the extension to execute.
- [struct ASAuthorizationProviderAuthorizationOperation](./asauthorizationproviderauthorizationoperation.md)
  A type that represents an authorization operation.
- [var authorizationOptions: [AnyHashable : Any]](./asauthorizationproviderextensionauthorizationrequest/authorizationoptions.md)
  A collection of options associated with the request.
### Getting Context
- [var callerBundleIdentifier: String](./asauthorizationproviderextensionauthorizationrequest/callerbundleidentifier.md)
  The bundle ID of the app making the request.
- [var callerTeamIdentifier: String](./asauthorizationproviderextensionauthorizationrequest/callerteamidentifier.md)
  The team identifier of the app making the request.
- [var localizedCallerDisplayName: String](./asauthorizationproviderextensionauthorizationrequest/localizedcallerdisplayname.md)
  The localized display name of the app making the request.
- [var isCallerManaged: Bool](./asauthorizationproviderextensionauthorizationrequest/iscallermanaged.md)
  A Boolean value that indicates whether the app making the request is managed.
- [var extensionData: [AnyHashable : Any]](./asauthorizationproviderextensionauthorizationrequest/extensiondata.md)
  Extension data from the Mobile Device Management (MDM) configuration.
### Interacting with the User
- [func presentAuthorizationViewController(completion: (Bool, (any Error)?) -> Void)](./asauthorizationproviderextensionauthorizationrequest/presentauthorizationviewcontroller%28completion%29.md)
  Asks the authorization service to show the extension’s view controller to the user.
- [var isUserInterfaceEnabled: Bool](./asauthorizationproviderextensionauthorizationrequest/isuserinterfaceenabled.md)
  Determines if user interface is available for the current request.
### Completing a Request
- [func complete(authorizationResult: ASAuthorizationProviderExtensionAuthorizationResult)](./asauthorizationproviderextensionauthorizationrequest/complete%28authorizationresult%29.md)
- [func complete()](./asauthorizationproviderextensionauthorizationrequest/complete%28%29.md)
  Indicates the requested authorization completed with no output.
- [func complete(httpAuthorizationHeaders: [String : String])](./asauthorizationproviderextensionauthorizationrequest/complete%28httpauthorizationheaders%29.md)
  Indicates the requested authorization succeeded with tokens in the HTTP headers.
- [func complete(httpResponse: HTTPURLResponse, httpBody: Data?)](./asauthorizationproviderextensionauthorizationrequest/complete%28httpresponse,httpbody%29.md)
  Indicates the requested authorization succeeded with an HTTP response.
- [func complete(error: any Error)](./asauthorizationproviderextensionauthorizationrequest/complete%28error%29.md)
  Indicates the requested authorization failed.
### Canceling a Request
- [func doNotHandle()](./asauthorizationproviderextensionauthorizationrequest/donothandle%28%29.md)
  Indicates the request wasn’t handled.
- [func cancel()](./asauthorizationproviderextensionauthorizationrequest/cancel%28%29.md)
  Cancels the request, for example, because the user taps a cancel button.
### Supporting Platform Single Sign-On
- [var loginManager: ASAuthorizationProviderExtensionLoginManager?](./asauthorizationproviderextensionauthorizationrequest/loginmanager.md)
  The manager that interacts with Platform SSO.
### Instance Properties
- [var callerAuditToken: Data](./asauthorizationproviderextensionauthorizationrequest/calleraudittoken.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Starting or Canceling a Request
- [func beginAuthorization(with: ASAuthorizationProviderExtensionAuthorizationRequest)](./asauthorizationproviderextensionauthorizationrequesthandler/beginauthorization%28with%29.md)
  Tells your request handler to authorize the given request.
- [func cancelAuthorization(with: ASAuthorizationProviderExtensionAuthorizationRequest)](./asauthorizationproviderextensionauthorizationrequesthandler/cancelauthorization%28with%29.md)
  Tells your request handler to cancel the authorization of the given request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest)*