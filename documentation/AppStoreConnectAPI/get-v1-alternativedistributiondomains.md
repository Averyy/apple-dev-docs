# List Alternative Distribution Domains

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all the alternative distribution domains for your account.

**Availability**:
- App Store Connect API 3.4.1+

#### Discussion

##### Example Request and Response

**Request**:

```

```

**Response**:

```json

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/alternativeDistributionDomains`

## Parameters

### Query Parameters

- `fields[alternativeDistributionDomains]` ([string]): Additional fields to include for each alternative distribution domains resource returned by the response.

  **Allowed Values**: `domain`, `referenceName`, `createdDate`
- `limit` (integer): The maximum number of alternative distribution domains resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AlternativeDistributionDomainsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing domains
- [Add an Alternative Distribution Domain](./post-v1-alternativedistributiondomains.md)
  Add an alternative distribution domain to your account.
- [Read Alternative Distribution Domain Information](./get-v1-alternativedistributiondomains-_id_.md)
  Read information for a specific alternative distribution domain.
- [Delete an Alternative Distribution Domain](./delete-v1-alternativedistributiondomains-_id_.md)
  Delete the alternative distribution search domain for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-alternativedistributiondomains)*