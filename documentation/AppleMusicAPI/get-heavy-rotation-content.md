# Get Heavy Rotation Content

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the resources in heavy rotation for the user.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of [`Resource`](resource.md) objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

## See Also

- [object Resource](resource.md)
  A resource—such as an album, song, or playlist.
- [Get Recently Played Resources](get-recently-played-resources.md)
  Fetch the recently played resources for the user.
- [Get Recently Played Tracks](get-v1-me-recent-played-tracks.md)
  Fetch the recently played tracks for the user.
- [Get Recently Played Stations](get-recently-played-stations.md)
  Fetch recently played radio stations for the user.
- [Get Recently Added Resources](get-recently-added-resources.md)
  Fetch the resources recently added to the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-heavy-rotation-content)*