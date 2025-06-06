# Get a Catalog Playlist's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a playlist’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object Playlists](playlists.md)
  A resource object that represents a playlist.
- [object PlaylistsResponse](playlistsresponse.md)
  The response to a playlists request.
- [Get a Catalog Playlist](get-a-catalog-playlist.md)
  Fetch a playlist by using its identifier.
- [Get a Catalog Playlist’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-6i3ek.md)
  Fetch related resources for a single playlist’s relationship view.
- [Get Multiple Catalog Playlists](get-multiple-catalog-playlists.md)
  Fetch one or more playlists by using their identifiers.
- [Get Charts Playlists by Storefront Value](get-charts-playlists-by-storefront-value.md)
  Fetch one or more Charts Playlists by using their Storefront value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-707nb)*