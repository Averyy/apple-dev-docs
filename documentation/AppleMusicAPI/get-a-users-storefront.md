# Get a User's Storefront

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a storefront for a specific user.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single [`Storefronts`](storefronts.md) object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

## See Also

- [object Storefronts](storefronts.md)
  A resource object that represents a storefront, an Apple Music and iTunes Store territory that the content is available in.
- [object StorefrontsResponse](storefrontsresponse.md)
  The response to a storefront request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-user's-storefront)*