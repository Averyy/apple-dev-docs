# Performing a preauthentication request

**Framework**: Authentication Services

Request and process a preauthentication for dynamic WS-Trust authentication.

#### Overview

Federation enables authentication between security domains, such as from a local identity provider (IdP) to a cloud IdP. Platform SSO supports federated authentication with WS-Trust and dynamic WS-Trust. Use dynamic WS-Trust when the federation for a user can change.

The system sends a preauthentication request when the [`federationType`](asauthorizationproviderextensionloginconfiguration/federationtype-swift.property.md) is [`ASAuthorizationProviderExtensionLoginConfiguration.FederationType.dynamicWSTrust`](asauthorizationproviderextensionloginconfiguration/federationtype-swift.enum/dynamicwstrust.md). It uses this request to determine whether the user is federated and to receive the [`federationMEXURL`](asauthorizationproviderextensionloginconfiguration/federationmexurl.md) for the metadata exchange data (MEX) request. For more information, see [`Performing a WS-Trust metadata exchange data (MEX) request`](performing-a-ws-trust-metadata-exchange-data-mex-request.md).

If the user isn’t federated, the login proceeds as a normal password authentication to the IdP.

##### Create the Preauthentication Network Request

The following table specifies the query string parameters that the system uses to create a preauthentication network request:

| Key | Value | Notes |
| --- | --- | --- |
| `user` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | The login user name. If not set, the system uses the local account name. |
| [`customFederationUserPreauthenticationRequestValues`](asauthorizationproviderextensionloginconfiguration/customfederationuserpreauthenticationrequestvalues.md) |  | Optional. If present, adds the key value pairs to the request. |

The request is an HTTP GET to the login configuration [`federationUserPreauthenticationURL`](asauthorizationproviderextensionloginconfiguration/federationuserpreauthenticationurl.md), as shown here:

```http
GET /oauth2/discovery?user=foo@example.com HTTP/1.1
Host: auth.example.com
Accept: application/json
client-request-id: DCAB01D3-B1FE-4E1C-802F-B3EBDCDF9E67
```

##### Receive the Preauthentication Network Response

If the http status is `200`, the response body loads as JSON. If the body is valid JSON, then the system evaluates the [`federationPredicate`](asauthorizationproviderextensionloginconfiguration/federationpredicate.md) to determine whether the user is federated.

If the user is federated, the system uses the [`federationMEXURLKeypath`](asauthorizationproviderextensionloginconfiguration/federationmexurlkeypath.md) to select the URL to use for federation. If the [`federationMEXURLKeypath`](asauthorizationproviderextensionloginconfiguration/federationmexurlkeypath.md) isn’t specified, the system uses the default value `federation_metadata_url`. The system sends the MEX request to this URL to determine the WS-Trust version to use.

## See Also

- [Obtaining a server nonce](obtaining-a-server-nonce.md)
  Request and process a server nonce to verify communication and detect replays.
- [Performing a WS-Trust metadata exchange data (MEX) request](performing-a-ws-trust-metadata-exchange-data-mex-request.md)
  Send and process a WS-Trust MEX request to determine the version and URLs for authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/performing-a-preauthentication-request)*