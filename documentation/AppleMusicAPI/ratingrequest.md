# RatingRequest

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A request containing the data for a rating.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object RatingRequest
```

## Topics

### Related Objects
- [object RatingRequest.Attributes](./ratingrequest/attributes-data.dictionary.md)
  The attributes for a rating request object.

## Properties

- `attributes` (RatingRequest.Attributes) *(required)*: The dictionary that includes the value for the resource’s rating.
- `type` (string) *(required)*: The type of the payload.

  **Allowed Values**: `ratings`

## See Also

### Handling the Response
- [object Ratings](./ratings.md)
  An object that represents a rating for a resource.
- [object RatingsResponse](./ratingsresponse.md)
  The response to a request for a rating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/ratingrequest)*