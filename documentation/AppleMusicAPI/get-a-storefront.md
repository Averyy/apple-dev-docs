# Get a Storefront

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a single storefront by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single [`Storefronts`](storefronts.md) object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

##### Example

## See Also

- [object Storefronts](storefronts.md)
  A resource object that represents a storefront, an Apple Music and iTunes Store territory that the content is available in.
- [object StorefrontsResponse](storefrontsresponse.md)
  The response to a storefront request.
- [Get Multiple Storefronts](get-multiple-storefronts.md)
  Fetch one or more storefronts by using their identifiers.
- [Get All Storefronts](get-all-storefronts.md)
  Fetch all the storefronts in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-storefront)*