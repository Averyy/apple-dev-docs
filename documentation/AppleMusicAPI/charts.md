# Get Catalog Charts

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more charts from the Apple Music Catalog.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the response contains an object where `results` contains chart collections. The members for the collections are the chart types in the request and the values are `Chart` objects. The `data` member of each `Chart` object contains an array of the corresponding resource ordered by popularity. For example, if the request contains the `songs` chart type, the object contains a `songs` member with a value that is a `Chart` object containing `Song` objects. This may be a paginated response. For more information, see `Fetch Resources by Page`.

If unsuccessful, the HTTP status code indicates the error and the details are in the errors array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object ChartResponse](chartresponse.md)
  The response to a request for a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/charts)*