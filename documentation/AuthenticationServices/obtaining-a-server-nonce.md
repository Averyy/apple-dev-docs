# Obtaining a server nonce

**Framework**: Authentication Services

Request and process a server nonce to verify communication and detect replays.

#### Overview

The login request, refresh request, and key requests use the server nonce so the identity provider (IdP) can verify it’s communicating to a live client. The IdP can also use the server nonce for replay detection.

##### Create the Server Nonce Network Request

The following table specifies the header parameters that the system uses to create a server nonce request:

| Key | Value | Notes |
| --- | --- | --- |
| `grant_type` | `srv_challenge` | Required. |
| [`customNonceRequestValues`](asauthorizationproviderextensionloginconfiguration/customnoncerequestvalues.md) |  | Optional. If present, adds the key value pairs to the request. |
| `client-request-id` | `UUID` | Required. A unique identifier for the request. |

The server nonce request is an HTTP POST to the login configuration [`nonceEndpointURL`](asauthorizationproviderextensionloginconfiguration/nonceendpointurl.md), as shown in the following example:

```http
POST /oauth2/token HTTP/1.1
Host: auth.example.com
Accept: application/json
Content-Type: application/x-www-form-urlencoded
client-request-id: DCAB01D3-B1FE-4E1C-802F-B3EBDCDF9E67
grant_type=srv_challenge
```

##### Receive the Server Nonce Network Response

If the http status is `200`, the response body loads as JSON. If the body is valid JSON, the system pulls the server nonce from the response using the login configuration [`nonceResponseKeypath`](asauthorizationproviderextensionloginconfiguration/nonceresponsekeypath.md) or the default value `Nonce`.

Platform SSO doesn’t validate the token and treats it as an opaque value.

## See Also

- [Performing a preauthentication request](performing-a-preauthentication-request.md)
  Request and process a preauthentication for dynamic WS-Trust authentication.
- [Performing a WS-Trust metadata exchange data (MEX) request](performing-a-ws-trust-metadata-exchange-data-mex-request.md)
  Send and process a WS-Trust MEX request to determine the version and URLs for authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/obtaining-a-server-nonce)*