# Delete an Alternative Distribution Domain

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete the alternative distribution search domain for an app.

**Availability**:
- App Store Connect API 3.4.1+

#### Discussion

##### Example Request and Response

**Request**:

```
DELETE https://api.appstoreconnect.apple.com/v1/alternativeDistributionDomains/{id}
```

**Response**:

```json
204
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/alternativeDistributionDomains/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the alternative distribution domain resource ID from the [`List Alternative Distribution Domains`](./get-v1-alternativedistributiondomains.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing domains
- [Add an Alternative Distribution Domain](./post-v1-alternativedistributiondomains.md)
  Add an alternative distribution domain to your account.
- [Read Alternative Distribution Domain Information](./get-v1-alternativedistributiondomains-_id_.md)
  Read information for a specific alternative distribution domain.
- [List Alternative Distribution Domains](./get-v1-alternativedistributiondomains.md)
  List all the alternative distribution domains for your account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-alternativedistributiondomains-_id_)*