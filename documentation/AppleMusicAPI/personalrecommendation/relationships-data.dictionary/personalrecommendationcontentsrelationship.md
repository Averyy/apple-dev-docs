# PersonalRecommendation.Relationships.PersonalRecommendationContentsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the recommendation to its recommended content.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object PersonalRecommendation.Relationships.PersonalRecommendationContentsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Resource]) *(required)*: A list of recommended candidates that are a mixture of albums and playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/personalrecommendation/relationships-data.dictionary/personalrecommendationcontentsrelationship)*