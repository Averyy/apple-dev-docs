# Get Multiple Catalog Curators

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more curators by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of `Curator` objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object Curators](curators.md)
  A resource object that represents a curator.
- [object CuratorsResponse](curatorsresponse.md)
  The response to a request for curators.
- [Get a Catalog Curator](get-a-catalog-curator.md)
  Fetch a curator by using the curator’s identifier.
- [Get a Catalog Curator's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-1091z.md)
  Fetch a curator’s relationship by using its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-catalog-curators)*