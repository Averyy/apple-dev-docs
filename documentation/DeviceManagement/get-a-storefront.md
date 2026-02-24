# Get a Storefront

**Framework**: Device Management  
**Kind**: httpRequest

Fetch a single storefront by using its identifier.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Endpoint

`GET https://api.ent.apple.com/v1/storefronts/{id}`

## Parameters

- `extend` ([string]): A list of attribute extensions to apply to resources in the response. Classifier (optional): A resource type to apply the parameter to.
- `include` ([string]): A list of relationship names to include for resources in the response. Classifier (optional): A resource type to apply the parameter to.
- `l` (string): The localization to use, which you specify with a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `relate` ([string]): A list of relationship names to relate for resources in the response. Classifier (optional): A resource type to apply the parameter to.
- `platform` (string) *(required)*: The platform the user-facing app is running on. You use this to get metadata for the specified platform.

## See Also

- [Get Multiple Storefronts](get-multiple-storefronts.md)
  Fetch one or more storefronts by using their identifiers.
- [Get All Storefronts](get-all-storefronts.md)
  Fetch all the storefronts in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-a-storefront)*