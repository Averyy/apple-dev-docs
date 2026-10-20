# Read the Pass Type Id Information of a Certificate

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/certificates/{id}/passTypeId`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `certificateContent`, `certificateType`, `csrContent`, `displayName`, `expirationDate`, `name`, `passTypeId`, `platform`, `serialNumber`
- `fields[passTypeIds]` ([string]): **Allowed Values**: `certificates`, `identifier`, `name`
- `include` ([string]): **Allowed Values**: `certificates`
- `limit[certificates]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`PassTypeIdResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/read-the-pass-type-id-information-of-a-certificate)*