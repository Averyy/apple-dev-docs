# Generate a Maps token

**Framework**: Apple Maps Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Returns a JWT maps access token that you use to call the service API.

**Availability**:
- Apple Maps Server API 1.2+

## Mentions

- [Creating and using tokens with Maps Server API](./creating-and-using-tokens-with-maps-server-api.md)

## Discussion

### Example

**Request**:

```
curl -si -H "Authorization: Bearer <maps_auth_token>" "https://maps-api.apple.com/v1/token"
```

**Response**:

```json
{
  "accessToken": "<maps_access_token>",
  "expiresInSeconds": 1800
}
```

## Endpoint

`GET https://maps-api.apple.com/v1/token`

## Responses

- `200` OK (`TokenResponse`, `application/json`): A response that indicates the authorization request is successful. The dictionary that accompanies the response contains a maps access token and an integer that indicates the time in seconds until the token expires.
- `401` Unauthorized (`ErrorResponse`, `application/json`): An error response that indicates the maps token is missing or invalid. The dictionary that accompanies the error may contain additional details about the error.
- `429` (`ErrorResponse`, `application/json`): An [`ErrorResponse`](./errorresponse.md) object that indicates the call exceeds the daily service call quota for the authorization token presented. The app should try again later. If your app requires a larger daily quota, submit a [quota increase request form](https://developer.apple.com/contact/request/mapkitjs/).
- `500` Internal Server Error (`ErrorResponse`, `application/json`): An error that indicates the server can’t complete the request. The dictionary that accompanies the error may contain additional details about the error.

## See Also

### Essentials
- [Creating and using tokens with Maps Server API](./creating-and-using-tokens-with-maps-server-api.md)
  Sign JSON Web Tokens to use Maps Server API and debug common signing errors.
- [Creating a Maps identifier and a private key](./creating-a-maps-identifier-and-a-private-key.md)
  Create a Maps identifier and a private key before generating tokens for MapKit JS.
- [Debugging an Invalid token](./debugging-an-invalid-token.md)
  Inspect the JavaScript console logs, the token, and events to determine why a token is invalid.
- [Common objects](./common-objects.md)
  Understand the common JSON objects that API responses contain.
- [Integrating the Apple Maps Server API into Java server applications](./integrating-the-apple-maps-server-api-into-java-server-applications.md)
  Streamline your app’s API by moving georelated searches from inside your app to your server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/-v1-token)*