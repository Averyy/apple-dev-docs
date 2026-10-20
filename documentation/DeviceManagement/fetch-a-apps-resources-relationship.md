# Fetch a apps resource's relationship

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- VPP License Management 2.2+

## Endpoint

`GET https://api.ent.apple.com/v1/catalog/{storefront}/apps/{id}/{relationship}`

## Parameters

### Path Parameters

- `id` (string) *(required)*
- `relationship` (string) *(required)*: **Allowed Values**: `genres`
- `storefront` (string) *(required)*

### Query Parameters

- `additionalPlatforms` ([string]): **Allowed Values**: `appletv`, `ipad`, `iphone`, `mac`, `realityDevice`, `web`
- `extend` ([string]): **Allowed Values**: `description`, `fileSizeByDevice`, `languageList`, `latestVersionInfo`, `privacyPolicyUrl`, `requirementsByDeviceFamily`, `screenshotsByType`, `supportURLForLanguage`, `versionHistory`, `websiteUrl`
- `include` ([string])
- `l` (string)
- `limit` (integer)
- `platform` (string) *(required)*: **Allowed Values**: `appletv`, `ipad`, `iphone`, `mac`, `realityDevice`, `web`
- `relate` ([string])

## Responses

- `200` OK (`RelationshipResponse`, `application/json`)
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`)
- `500` Internal Server Error (`ErrorsResponse`, `application/json`)

## See Also

### Fetching relationships
- [Fetch a books resource's relationship](./fetch-a-books-resources-relationship.md)
- [object RelationshipResponse](./relationshipresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-a-apps-resource's-relationship)*