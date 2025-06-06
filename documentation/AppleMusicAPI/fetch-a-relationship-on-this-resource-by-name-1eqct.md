# Get a Catalog Activity's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch an activity’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single `Activity.Relationships` object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object Activities](activities.md)
  A resource object that represents an activity curator.
- [object ActivitiesResponse](activitiesresponse.md)
  The response to a request for activities.
- [Get a Catalog Activity](get-a-catalog-activity.md)
  Fetch an activity by using its identifier.
- [Get Multiple Catalog Activities](get-multiple-catalog-activities.md)
  Fetch one or more activities by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-1eqct)*