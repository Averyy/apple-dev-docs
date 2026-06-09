# Get All Storefronts

**Framework**: Device Management  
**Kind**: httpRequest

Fetch all the storefronts in alphabetical order.

**Availability**:
- VPP License Management 2.1+

## Endpoint

`GET https://api.ent.apple.com/v1/storefronts`

## Parameters

- `extend` ([string]): A list of attribute extensions to apply to resources in the response. Classifier (optional): A resource type to apply the parameter to.
- `include` ([string]): A list of relationship names to include for resources in the response. Classifier (optional): A resource type to apply the parameter to.
- `l` (string): The localization to use, which you specify with a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): A limit to apply to the results. Classifier (optional): A relationship name to apply the limit to.
- `offset` (string): The offset to use for a paginated request.
- `relate` ([string]): A list of relationship names to relate for resources in the response. Classifier (optional): A resource type to apply the parameter to.
- `platform` (string) *(required)*: The platform the user-facing app is running on. You use this to get metadata for the specified platform.

## See Also

- [Get a Storefront](get-a-storefront.md)
  Fetch a single storefront by using its identifier.
- [Get Multiple Storefronts](get-multiple-storefronts.md)
  Fetch one or more storefronts by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-all-storefronts)*