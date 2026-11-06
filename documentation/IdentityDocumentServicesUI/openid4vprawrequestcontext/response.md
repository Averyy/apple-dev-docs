# OpenID4VPRawRequestContext.Response

**Framework**: IdentityDocumentServicesUI  
**Kind**: struct  
**Role**: Structure

An OpenID4VP response to send to the relying party.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
struct Response
```

## Overview

Create a response with [`init(responseData:)`](./response/init%28responsedata%29.md), and pass it to [`sendResponse(_:)`](./sendresponse%28_%29.md).

## Topics

### Creating a response
- [init(responseData: Data)](./response/init%28responsedata%29.md)
  Creates an OpenID4VP response.
### Accessing the response data
- [let responseData: Data](./response/responsedata.md)
  The OpenID4VP authorization response.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Responding to the request
- [func sendResponse(OpenID4VPRawRequestContext.Response)](./sendresponse%28_%29.md)
  Sends an OpenID4VP response to the relying party.
- [func cancel()](./cancel%28%29.md)
  Cancels the current request from the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/openid4vprawrequestcontext/response)*