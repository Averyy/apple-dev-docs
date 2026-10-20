# ErrorsResponse

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The collection of errors that occurred while processing the request.

**Availability**:
- VPP License Management 2.1+

## Declaration

```
object ErrorsResponse
```

## Properties

- `errors` ([Error]) *(required)*: An error that occurred while processing the request.

## See Also

### Interpreting responses
- [object ResourceCollectionResponse](./resourcecollectionresponse.md)
  A response that contains the resource objects for the request.
- [object ResultsResponse](./resultsresponse.md)
  A response that contains the resource objects for the request.
- [object AppsResponse](./appsresponse.md)
  A response that contains the resource objects for the request.
- [object BooksResponse](./booksresponse.md)
  A response that contains the resource objects for the request.
- [object UnauthorizedResponse](./unauthorizedresponse.md)
  A response that indicates an incorrect authorization header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorsresponse)*