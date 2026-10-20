# Create a routing app coverage

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Attach a routing app coverage file to an App Store version.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/routingAppCoverages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `RoutingAppCoverageCreateRequest`

## Responses

- `201` Created (`RoutingAppCoverageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and Creating Routing App Coverages
- [Read the routing app coverage information of an app store version](./get-v1-appstoreversions-_id_-routingappcoverage.md)
  Get the routing app coverage file that is associated with a specific App Store version
- [Read routing app coverage information](./get-v1-routingappcoverages-_id_.md)
  Get information about the routing app coverage file and its upload and processing status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-routingappcoverages)*