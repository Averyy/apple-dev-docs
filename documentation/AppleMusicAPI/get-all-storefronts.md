# Get All Storefronts

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all the storefronts in alphabetical order.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains one or more [`Storefronts`](storefronts.md) objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

##### Example

## See Also

- [object Storefronts](storefronts.md)
  A resource object that represents a storefront, an Apple Music and iTunes Store territory that the content is available in.
- [object StorefrontsResponse](storefrontsresponse.md)
  The response to a storefront request.
- [Get a Storefront](get-a-storefront.md)
  Fetch a single storefront by using its identifier.
- [Get Multiple Storefronts](get-multiple-storefronts.md)
  Fetch one or more storefronts by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-storefronts)*