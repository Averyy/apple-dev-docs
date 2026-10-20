# PersonalRecommendation.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The relationships for a recommendation resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object PersonalRecommendation.Relationships
```

## Topics

### Related Objects
- [object PersonalRecommendation.Relationships.PersonalRecommendationContentsRelationship](./relationships-data.dictionary/personalrecommendationcontentsrelationship.md)
  A relationship from the recommendation to its recommended content.

## Properties

- `contents` (PersonalRecommendation.Relationships.PersonalRecommendationContentsRelationship): The contents associated with the content recommendation type. By default, `contents` includes objects.

  Fetch limits: 10 default, 10 maximum.

## See Also

### Related Objects
- [object PersonalRecommendation.Attributes](./attributes-data.dictionary.md)
  The attributes for a recommendation resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/personalrecommendation/relationships-data.dictionary)*