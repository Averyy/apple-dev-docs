# Get a Storefront

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch a single storefront by using its identifier.

**Availability**:
- VPP License Management 2.1+

## Endpoint

`GET https://api.ent.apple.com/v1/storefronts/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The ID of the resource to fetch.

### Query Parameters

- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

  Classifier (optional): A resource type to apply the parameter to.
- `include` ([string]): A list of relationship names to include for resources in the response.

  Classifier (optional): A resource type to apply the parameter to.
- `l` (string): The localization to use, which you specify with a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `relate` ([string]): A list of relationship names to relate for resources in the response.

  Classifier (optional): A resource type to apply the parameter to.
- `platform` (string) *(required)*: The platform the user-facing app is running on. You use this to get metadata for the specified platform.

  **Allowed Values**: `appletv`, `ipad`, `iphone`, `mac`, `realityDevice`, `web`

## Responses

- `200` OK (`StorefrontsResponse`, `application/json`): The collection of storefronts for the request.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Requesting a catalog storefront
- [Get Multiple Storefronts](./get-multiple-storefronts.md)
  Fetch one or more storefronts by using their identifiers.
- [Get All Storefronts](./get-all-storefronts.md)
  Fetch all the storefronts in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-a-storefront)*