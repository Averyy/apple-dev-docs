# PersonalRecommendation.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The attributes for a recommendation resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object PersonalRecommendation.Attributes
```

## Topics

### Attribute Objects
- [object PersonalRecommendation.Attributes.Reason](./attributes-data.dictionary/reason-data.dictionary.md)
  An object that represents the reason for a personal recommendation.
- [object PersonalRecommendation.Attributes.Title](./attributes-data.dictionary/title-data.dictionary.md)
  An object that represents the title of a personal recommendation.

## Properties

- `isGroupRecommendation` (boolean) *(required)* *(deprecated)*: Whether the recommendation is of group type.
- `kind` (string) *(required)*: The type of recommendation. Possible values are:

  - **`music-recommendations`**: A recommendation for music content.
  - **`recently-played`**: A recommendation based on recently played content.
  - **`unknown`**: A generic recommendation type.

  **Allowed Values**: `music-recommendations`, `recently-played`, `unknown`
- `nextUpdateDate` (string) *(required)*: The next date in UTC format for updating the recommendation.
- `reason` (PersonalRecommendation.Attributes.Reason): The localized reason for the recommendation.
- `resourceTypes` ([string]) *(required)*: The resource types supported by the recommendation.
- `title` (PersonalRecommendation.Attributes.Title): The localized title for the recommendation.

## See Also

### Related Objects
- [object PersonalRecommendation.Relationships](./relationships-data.dictionary.md)
  The relationships for a recommendation resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/personalrecommendation/attributes-data.dictionary)*