# Service Configuration

**Framework**: Device Management  
**Kind**: httpRequest

Provides the full list of web service URLs and a list of possible error numbers.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Clients should use this endpoint every 5 minutes to retrieve the list of service URLs, because the URLs may change. This endpoint exists to provide a level-of-service discovery, so service URLs can be changed in a transparent way.

##### Example Response

## Topics

### Response
- [object VppServiceConfigResponse](vppserviceconfigresponse.md)
  The response with the service configuration.
### Product Metadata
- [Getting App and Book Information (Legacy)](getting-app-and-book-information-legacy.md)
  Use a web service to find details about apps and books to show to your users.

## See Also

- [Client Configuration](client-configuration.md)
  Store client-specific information on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/service-configuration)*