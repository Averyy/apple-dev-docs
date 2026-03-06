# PersonalRecommendation.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary

The relationships for a recommendation resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object PersonalRecommendation.Relationships
```

## Topics

### Related Objects
- [object PersonalRecommendation.Relationships.PersonalRecommendationContentsRelationship](personalrecommendation/relationships-data.dictionary/personalrecommendationcontentsrelationship.md)
  A relationship from the recommendation to its recommended content.

## Properties

- `contents` (PersonalRecommendation.Relationships.PersonalRecommendationContentsRelationship): The contents associated with the content recommendation type. By default, `contents` includes objects. Fetch limits: 10 default, 10 maximum.

## See Also

- [object PersonalRecommendation.Attributes](personalrecommendation/attributes-data.dictionary.md)
  The attributes for a recommendation resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/personalrecommendation/relationships-data.dictionary)*