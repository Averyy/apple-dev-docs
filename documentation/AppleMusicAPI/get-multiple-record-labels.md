# Get Multiple Record Labels

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more record labels by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object RecordLabels](recordlabels.md)
  A resource object that represents a record label.
- [object RecordLabelsResponse](recordlabelsresponse.md)
  The response to a request for record labels.
- [Get a Catalog Record Label](get-a-record-label.md)
  Fetch a record label by using its identifier.
- [Get a Catalog Record Label’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-5uhxd.md)
  Fetch related resources for a single record label’s relationship view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-record-labels)*