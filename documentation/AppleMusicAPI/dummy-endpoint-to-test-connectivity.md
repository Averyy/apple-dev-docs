# Placeholder Endpoint to Test Connectivity

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- Apple Music 1.0+

## Endpoint

`GET https://api.music.apple.com/v1/test`

## Parameters

### Query Parameters

- `l` (string)

## Responses

- `200` OK (`EmptyBodyResponse`, `application/json`)
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`)
- `500` Internal Server Error (`ErrorsResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/dummy-endpoint-to-test-connectivity)*