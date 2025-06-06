# Get a Recommendation

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a recommendation by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single `Recommendation` object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

## See Also

- [object PersonalRecommendation](personalrecommendation.md)
  A resource object that represents recommended resources for a user calculated using their selected preferences.
- [object PersonalRecommendationResponse](personalrecommendationresponse.md)
  The response to a request for personal recommendations.
- [Get a Recommendation Relationship Directly by Name](get-a-relationship-on-the-recommendation.md)
  Fetch a recommendation’s relationship by using its identifier.
- [Get Multiple Recommendations](get-multiple-recommendations.md)
  Fetch one or more recommendations by using their identifiers.
- [Get Default Recommendations](get-all-recommendations.md)
  Fetch default recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-recommendation)*