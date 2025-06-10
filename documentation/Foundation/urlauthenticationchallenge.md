# URLAuthenticationChallenge

**Framework**: Foundation  
**Kind**: class

A challenge from a server requiring authentication from the client.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class URLAuthenticationChallenge
```

#### Overview

Your app receives authentication challenges in various [`URLSession`](urlsession.md), [`NSURLConnection`](nsurlconnection.md), and [`NSURLDownload`](nsurldownload.md) delegate methods, such as [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md). These objects provide the information you’ll need when deciding how to handle a server’s request for authentication.

At the core of that authentication challenge is a  that defines the type of authentication being requested, the host and port number, the networking protocol, and (where applicable) the authentication realm (a group of related URLs on the same server that share a single set of credentials).

## Topics

### Creating an authentication challenge instance
- [init(authenticationChallenge: URLAuthenticationChallenge, sender: any URLAuthenticationChallengeSender)](urlauthenticationchallenge/init(authenticationchallenge:sender:).md)
  Creates an authentication challenge from an existing challenge instance.
- [init(protectionSpace: URLProtectionSpace, proposedCredential: URLCredential?, previousFailureCount: Int, failureResponse: URLResponse?, error: (any Error)?, sender: any URLAuthenticationChallengeSender)](urlauthenticationchallenge/init(protectionspace:proposedcredential:previousfailurecount:failureresponse:error:sender:).md)
  Initializes an authentication challenge from parameters you provide.
### Inspecting the authentication challenge
- [var protectionSpace: URLProtectionSpace](urlauthenticationchallenge/protectionspace.md)
  The receiver’s protection space.
### Getting properties of previous authentication attempts
- [var failureResponse: URLResponse?](urlauthenticationchallenge/failureresponse.md)
  The URL response object representing the last authentication failure.
- [var previousFailureCount: Int](urlauthenticationchallenge/previousfailurecount.md)
  The receiver’s count of failed authentication attempts.
- [var proposedCredential: URLCredential?](urlauthenticationchallenge/proposedcredential.md)
  The proposed credential for this challenge.
### Getting authentication errors
- [var error: (any Error)?](urlauthenticationchallenge/error.md)
  The error object representing the last authentication failure.
### Legacy
- [var sender: (any URLAuthenticationChallengeSender)?](urlauthenticationchallenge/sender.md)
  The sender of the challenge.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Handling an authentication challenge](handling-an-authentication-challenge.md)
  Respond appropriately when a server demands authentication for a URL request.
- [class URLCredential](urlcredential.md)
  `A`n authentication credential consisting of information specific to the type of credential and the type of persistent storage to use, if any.
- [class URLCredentialStorage](urlcredentialstorage.md)
  The manager of a shared credentials cache.
- [class URLProtectionSpace](urlprotectionspace.md)
  A server or an area on a server, commonly referred to as a realm, that requires authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge)*