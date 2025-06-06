# Get a Catalog Apple Curator's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch an Apple curator’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single `AppleCurator.Relationships` object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object AppleCurators](applecurators.md)
  A resource object that represents an Apple curator.
- [object AppleCuratorsResponse](applecuratorsresponse.md)
  The response to a request for Apple curators.
- [Get a Catalog Apple Curator](get-a-catalog-apple-curator.md)
  Fetch an Apple curator by using the curator’s identifier.
- [Get Multiple Catalog Apple Curators](get-multiple-catalog-apple-curators.md)
  Fetch one or more Apple curators by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-9aupk)*