# PersonalRecommendation

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A resource object that represents recommended resources for a user calculated using their selected preferences.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object PersonalRecommendation
```

## Topics

### Related Objects
- [object PersonalRecommendation.Attributes](./personalrecommendation/attributes-data.dictionary.md)
  The attributes for a recommendation resource.
- [object PersonalRecommendation.Relationships](./personalrecommendation/relationships-data.dictionary.md)
  The relationships for a recommendation resource.

## Properties

- `id` (string) *(required)*: The identifier for the recommendation.
- `type` (string) *(required)*: This value must always be `personal-recommendation`.

  **Allowed Values**: `personal-recommendation`
- `href` (string) *(required)*: The relative location for the recommendation resource.
- `attributes` (PersonalRecommendation.Attributes): The attributes for the recommendation.
- `relationships` (PersonalRecommendation.Relationships): The relationships for the playlist.

## See Also

### Handling the Response
- [object PersonalRecommendationResponse](./personalrecommendationresponse.md)
  The response to a request for personal recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/personalrecommendation)*