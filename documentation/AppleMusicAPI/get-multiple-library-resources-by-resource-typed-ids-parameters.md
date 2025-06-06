# Get Multiple Library Resources Using Resource-Typed ID Parameters

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more library resources by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

## See Also

- [object Resource](resource.md)
  A resource—such as an album, song, or playlist.
- [Get Multiple Catalog Resources Using Resource-Typed ID Parameters](get-multiple-catalog-resources-by-resource-typed-ids-parameters.md)
  Fetch one or more catalog resources by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-library-resources-by-resource-typed-ids-parameters)*