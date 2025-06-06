# Get a Catalog Artist

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch an artist by using the artist’s identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object Artists](artists.md)
  A resource object that represents the artist of an album where an artist can be one or more people.
- [object ArtistsResponse](artistsresponse.md)
  The response to an artists request.
- [Get a Catalog Artist's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-5akdm.md)
  Fetch an artist’s relationship by using its identifier.
- [Get a Catalog Artist’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-4kow5.md)
  Fetch related resources for a single artist’s relationship view.
- [Get Multiple Catalog Artists](get-multiple-catalog-artists.md)
  Fetch one or more artists by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-catalog-artist)*